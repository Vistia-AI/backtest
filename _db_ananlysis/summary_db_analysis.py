#!/usr/bin/env python3
"""
Trade Order Analysis Summary Script

This script analyzes trade order data from CSV files and generates a comprehensive
markdown report with summary statistics and raw data tables.

Usage:
    python summary_db_analysis.py

The script will process CSV files in the _db_ananlysis directory and generate
a trade_analysis_summary.md report.
"""

import pandas as pd
import os
import glob
from datetime import datetime
from typing import List, Dict, Any
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


def load_and_validate_csv(path: str) -> pd.DataFrame:
    """
    Load and validate CSV data from the given path.
    
    Args:
        path (str): Path to the CSV file
        
    Returns:
        pd.DataFrame: Validated DataFrame
    """
    try:
        if not os.path.exists(path):
            logger.error(f"File not found: {path}")
            return pd.DataFrame()
            
        df = pd.read_csv(path)
        
        # Validate required columns
        required_columns = ['strategy', 'symbol', 'open_time', 'order', 'price', 
                          'h_gt_count', 'l_lt_count', 'c_gt_count', 'c_lt_count']
        
        missing_columns = [col for col in required_columns if col not in df.columns]
        if missing_columns:
            logger.error(f"Missing required columns in {path}: {missing_columns}")
            return pd.DataFrame()
            
        # Remove rows with missing critical data
        df = df.dropna(subset=['order', 'price'])
        
        # Convert open_time to datetime if it's numeric
        if df['open_time'].dtype in ['int64', 'float64']:
            df['datetime'] = pd.to_datetime(df['open_time'], unit='s')
        else:
            df['datetime'] = pd.to_datetime(df['open_time'])
            
        # Convert numeric columns, handling empty strings
        numeric_columns = ['h_gt_count', 'l_lt_count', 'c_gt_count', 'c_lt_count']
        for col in numeric_columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
            
        logger.info(f"Successfully loaded {len(df)} rows from {path}")
        return df
        
    except Exception as e:
        logger.error(f"Error loading {path}: {str(e)}")
        return pd.DataFrame()


def calculate_order_stats(df: pd.DataFrame, order_type: str) -> Dict[str, Any]:
    """
    Calculate statistics for a specific order type.
    
    Args:
        df (pd.DataFrame): DataFrame containing order data
        order_type (str): 'BUY' or 'SELL'
        
    Returns:
        Dict[str, Any]: Dictionary containing calculated statistics
    """
    order_df = df[df['order'] == order_type].copy()
    
    if len(order_df) == 0:
        return {
            'total_count': 0,
            'performance_stats': {}
        }
    
    # Performance statistics for each metric
    performance_stats = {}
    metrics = ['h_gt_count', 'l_lt_count', 'c_gt_count', 'c_lt_count']
    
    for metric in metrics:
        valid_data = order_df[metric].dropna()
        if len(valid_data) > 0:
            performance_stats[metric] = {
                'total': valid_data.sum(),
                'min': valid_data.min(),
                'max': valid_data.max(),
                'avg': valid_data.mean(),
                'median': valid_data.median()
            }
        else:
            performance_stats[metric] = {
                'total': 0, 'min': 0, 'max': 0, 'avg': 0, 'median': 0
            }
    
    return {
        'total_count': len(order_df),
        'performance_stats': performance_stats
    }


def format_timestamp(timestamp) -> str:
    """
    Format timestamp to readable date string.
    
    Args:
        timestamp: Unix timestamp or datetime object
        
    Returns:
        str: Formatted date string
    """
    try:
        if pd.isna(timestamp):
            return "N/A"
        if isinstance(timestamp, (int, float)):
            return datetime.fromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
        else:
            return timestamp.strftime('%Y-%m-%d %H:%M:%S')
    except Exception:
        return "N/A"


def generate_markdown_table(stats: Dict[str, Any], order_type: str) -> str:
    """
    Generate markdown table for order statistics.
    
    Args:
        stats (Dict[str, Any]): Statistics dictionary
        order_type (str): 'BUY' or 'SELL'
        
    Returns:
        str: Markdown table string
    """
    if stats['total_count'] == 0:
        return f"### {order_type} Orders Summary\nNo {order_type} orders found.\n"
    
    table = f"### {order_type} Orders Summary\n"
    table += "| Metric | Total Count | Min | Max | Average | Median |\n"
    table += "|--------|-------------|-----|-----|---------|--------|\n"
    
    # Add order count row
    table += f"| Orders | {stats['total_count']} | - | - | - | - |\n"
    
    # Performance metrics
    metric_names = {
        'h_gt_count': 'High > Price',
        'l_lt_count': 'Low < Price', 
        'c_gt_count': 'Close > Price',
        'c_lt_count': 'Close < Price'
    }
    
    for metric, display_name in metric_names.items():
        if metric in stats['performance_stats']:
            perf_stats = stats['performance_stats'][metric]
            table += f"| {display_name} | {perf_stats['total']:.0f} | {perf_stats['min']:.1f} | {perf_stats['max']:.1f} | {perf_stats['avg']:.1f} | {perf_stats['median']:.1f} |\n"
    
    return table


def create_raw_data_table(df: pd.DataFrame, order_type: str) -> str:
    """
    Create raw data table for a specific order type.
    
    Args:
        df (pd.DataFrame): DataFrame containing order data
        order_type (str): 'BUY' or 'SELL'
        
    Returns:
        str: Markdown table string
    """
    order_df = df[df['order'] == order_type].copy()
    
    if len(order_df) == 0:
        return f"### All {order_type} Orders\nNo {order_type} orders found.\n"
    
    # Sort by date
    order_df = order_df.sort_values('datetime')
    
    table = f"### All {order_type} Orders\n"
    table += "| Strategy | Symbol | Date | Price | High>Price | Low<Price | Close>Price | Close<Price |\n"
    table += "|----------|--------|------|-------|------------|-----------|-------------|-------------|\n"
    
    for _, row in order_df.iterrows():
        strategy = row['strategy'] if pd.notna(row['strategy']) else "N/A"
        symbol = row['symbol'] if pd.notna(row['symbol']) else "N/A"
        date = format_timestamp(row['datetime'])
        price = f"{row['price']:.2f}" if pd.notna(row['price']) else "N/A"
        
        h_gt = f"{row['h_gt_count']:.0f}" if pd.notna(row['h_gt_count']) else "-"
        l_lt = f"{row['l_lt_count']:.0f}" if pd.notna(row['l_lt_count']) else "-"
        c_gt = f"{row['c_gt_count']:.0f}" if pd.notna(row['c_gt_count']) else "-"
        c_lt = f"{row['c_lt_count']:.0f}" if pd.notna(row['c_lt_count']) else "-"
        
        table += f"| {strategy} | {symbol} | {date} | {price} | {h_gt} | {l_lt} | {c_gt} | {c_lt} |\n"
    
    return table


def generate_trade_summary_report(csv_paths: List[str], output_path: str) -> None:
    """
    Generate comprehensive trade summary report from CSV files.
    
    Args:
        csv_paths (List[str]): List of CSV file paths
        output_path (str): Output markdown file path
    """
    logger.info(f"Starting trade summary report generation for {len(csv_paths)} files")
    
    all_data = []
    report_content = "# Trade Order Analysis Summary Report\n\n"
    report_content += f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n"
    
    # Process each CSV file
    for csv_path in csv_paths:
        logger.info(f"Processing {csv_path}")
        
        df = load_and_validate_csv(csv_path)
        if df.empty:
            logger.warning(f"Skipping empty or invalid file: {csv_path}")
            continue
            
        all_data.append(df)
        
        # File metadata
        filename = os.path.basename(csv_path)
        strategy = df['strategy'].iloc[0] if len(df) > 0 and pd.notna(df['strategy'].iloc[0]) else "Unknown"
        symbol = df['symbol'].iloc[0] if len(df) > 0 and pd.notna(df['symbol'].iloc[0]) else "Unknown"
        
        if len(df) > 0:
            date_range = f"{df['datetime'].min().strftime('%Y-%m-%d')} to {df['datetime'].max().strftime('%Y-%m-%d')}"
        else:
            date_range = "N/A"
            
        total_orders = len(df)
        
        # File section header
        report_content += f"## File: {filename}\n"
        report_content += f"- **Strategy**: {strategy}\n"
        report_content += f"- **Symbol**: {symbol}\n"
        report_content += f"- **Date Range**: {date_range}\n"
        report_content += f"- **Total Orders**: {total_orders}\n\n"
        
        # Calculate statistics
        buy_stats = calculate_order_stats(df, 'BUY')
        sell_stats = calculate_order_stats(df, 'SELL')
        
        # Generate tables
        report_content += generate_markdown_table(buy_stats, 'BUY')
        report_content += "\n"
        report_content += generate_markdown_table(sell_stats, 'SELL')
        report_content += "\n---\n\n"
    
    # Overall summary
    if all_data:
        combined_df = pd.concat(all_data, ignore_index=True)
        
        report_content += "## Overall Summary\n"
        report_content += f"- **Total Files Processed**: {len(all_data)}\n"
        report_content += f"- **Total Orders**: {len(combined_df)}\n"
        
        overall_buy_stats = calculate_order_stats(combined_df, 'BUY')
        overall_sell_stats = calculate_order_stats(combined_df, 'SELL')
        
        report_content += f"- **Total BUY Orders**: {overall_buy_stats['total_count']}\n"
        report_content += f"- **Total SELL Orders**: {overall_sell_stats['total_count']}\n\n"
        
        # Raw data tables
        report_content += "---\n\n## Raw Data Sources\n\n"
        report_content += create_raw_data_table(combined_df, 'BUY')
        report_content += "\n"
        report_content += create_raw_data_table(combined_df, 'SELL')
    
    # Write report to file
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(report_content)
        logger.info(f"Report successfully generated: {output_path}")
    except Exception as e:
        logger.error(f"Error writing report to {output_path}: {str(e)}")


def main():
    """
    Main function to execute the trade analysis.
    """
    # Find all CSV files in the _db_ananlysis directory
    csv_pattern = "_db_ananlysis/**/*.csv"
    csv_files = glob.glob(csv_pattern, recursive=True)
    
    if not csv_files:
        logger.error("No CSV files found in _db_ananlysis directory")
        return
    
    logger.info(f"Found {len(csv_files)} CSV files: {csv_files}")
    
    # Generate report
    output_file = "trade_analysis_summary.md"
    generate_trade_summary_report(csv_files, output_file)
    
    logger.info("Trade analysis completed successfully!")


if __name__ == "__main__":
    main()
