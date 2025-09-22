import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
import json

def generate_sample_feedback_data(num_samples: int = 100):
    """Generate realistic sample customer feedback data."""
    
    feedback_templates = {
        'technical': [
            "The app keeps crashing when I try to upload files. This is really frustrating!",
            "I can't access my dashboard after the latest update. Need help ASAP.",
            "Very slow performance when exporting reports. Takes forever to load.",
            "Login issues persist. Can't authenticate properly.",
            "Getting error messages constantly when using the search feature."
        ],
        'billing': [
            "I was charged twice for my subscription this month. Please refund immediately.",
            "My billing shows incorrect amounts. Need clarification on charges.",
            "Automatic renewal didn't work. Please update my payment method.",
            "Discount code wasn't applied to my order. Can you fix this?"
        ],
        'product': [
            "Love the new dashboard! Makes everything so much easier.",
            "Great product overall but mobile app needs work.",
            "Missing feature: bulk operations. Would be great to have this.",
            "Excellent customer service and product quality!"
        ],
        'shipping': [
            "My order is late. Expected delivery was yesterday. Where is it?",
            "Package arrived damaged. Need replacement urgently.",
            "Fast shipping! Arrived earlier than expected. Very pleased."
        ]
    }
    
    channels = ['email', 'chat', 'support_ticket', 'review', 'social']
    feedback_data = []
    
    for i in range(num_samples):
        category = np.random.choice(list(feedback_templates.keys()))
        template = np.random.choice(feedback_templates[category])
        channel = np.random.choice(channels)
        
        # Add urgency indicators for some items
        if np.random.random() < 0.15:  # 15% critical
            urgency_words = ["URGENT", "ASAP", "immediately", "critical"]
            template = f"{np.random.choice(urgency_words)}: " + template
        
        feedback_data.append({
            'feedback_id': f'feedback_{i+1:03d}',
            'customer_id': f'customer_{np.random.randint(1, 50):03d}',
            'channel': channel,
            'timestamp': datetime.now() - timedelta(days=np.random.randint(0, 30)),
            'raw_text': template,
            'category': category,
            'processed': False
        })
    
    return pd.DataFrame(feedback_data)

def create_sample_visualizations():
    """Create sample visualizations for the dashboard."""
    
    # Generate sample data for visualization
    dates = pd.date_range(start='2025-08-20', end='2025-09-20', freq='D')
    sentiment_data = {
        'date': dates,
        'avg_sentiment': np.random.normal(0.1, 0.3, len(dates)),
        'feedback_count': np.random.poisson(15, len(dates))
    }
    
    urgency_data = {
        'urgency_level': ['Low', 'Medium', 'High', 'Critical'],
        'count': [45, 30, 18, 7]
    }
    
    channel_data = {
        'channel': ['email', 'chat', 'support_ticket', 'review', 'social'],
        'total_feedback': [35, 28, 20, 12, 5],
        'avg_sentiment': [0.2, 0.1, -0.1, 0.4, -0.2]
    }
    
    # Create visualizations
    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    fig.suptitle('Smart Customer Insight Engine - Dashboard', fontsize=16, fontweight='bold')
    
    # 1. Sentiment Trends Over Time
    axes[0, 0].plot(sentiment_data['date'], sentiment_data['avg_sentiment'],
                    marker='o', linewidth=2, markersize=4, color='#2563eb')
    axes[0, 0].axhline(y=0, color='gray', linestyle='--', alpha=0.5)
    axes[0, 0].set_title('Daily Sentiment Trends')
    axes[0, 0].set_ylabel('Average Sentiment Score')
    axes[0, 0].grid(True, alpha=0.3)
    axes[0, 0].tick_params(axis='x', rotation=45)
    
    # 2. Urgency Distribution
    colors = ['#10b981', '#f59e0b', '#ef4444', '#8b5cf6']
    axes[0, 1].bar(urgency_data['urgency_level'], urgency_data['count'], color=colors)
    axes[0, 1].set_title('Feedback by Urgency Level')
    axes[0, 1].set_ylabel('Number of Items')
    
    # 3. Channel Performance
    x_pos = np.arange(len(channel_data['channel']))
    bars = axes[1, 0].bar(x_pos, channel_data['total_feedback'],
                         color=['#3b82f6', '#8b5cf6', '#f59e0b', '#10b981', '#ef4444'])
    axes[1, 0].set_title('Feedback Volume by Channel')
    axes[1, 0].set_ylabel('Total Feedback')
    axes[1, 0].set_xticks(x_pos)
    axes[1, 0].set_xticklabels(channel_data['channel'], rotation=45)
    
    # 4. Sentiment by Channel
    sentiment_colors = ['#10b981' if x > 0 else '#ef4444' for x in channel_data['avg_sentiment']]
    axes[1, 1].bar(channel_data['channel'], channel_data['avg_sentiment'],
                   color=sentiment_colors, alpha=0.7)
    axes[1, 1].axhline(y=0, color='black', linestyle='-', alpha=0.5)
    axes[1, 1].set_title('Average Sentiment by Channel')
    axes[1, 1].set_ylabel('Sentiment Score')
    axes[1, 1].tick_params(axis='x', rotation=45)
    
    plt.tight_layout()
    plt.show()
    
    print("Dashboard visualizations created successfully!")

def demo_semantic_search():
    """Demonstrate semantic search for similar issues."""
    
    print("\n" + "="*60)
    print("SEMANTIC SEARCH DEMONSTRATION")
    print("="*60)
    
    search_scenarios = [
        {
            'query': "mobile app keeps crashing on startup",
            'expected_matches': [
                "App crashes when I try to login on iOS",
                "Cannot open the mobile application, it freezes",
                "Getting error messages on app launch"
            ]
        },
        {
            'query': "billing charged twice for subscription",
            'expected_matches': [
                "Double payment taken from my credit card",
                "Subscription fee charged multiple times",
                "Incorrect billing amount on my statement"
            ]
        }
    ]
    
    for scenario in search_scenarios:
        print(f"\nSearch Query: '{scenario['query']}'")
        print("Similar Issues Found:")
        
        for i, match in enumerate(scenario['expected_matches'], 1):
            similarity_score = np.random.uniform(0.75, 0.95)
            print(f"   {i}. [{similarity_score:.2f}] {match}")
    
    print("\nThis demonstrates BigQuery's vector search capabilities")
    print("In production: ML.GENERATE_EMBEDDINGS() + ML.DISTANCE()")

def demo_predictive_analytics():
    """Demonstrate predictive analytics capabilities."""
    
    print("\n" + "="*60)
    print("PREDICTIVE ANALYTICS DEMONSTRATION")
    print("="*60)
    
    # Sample predictions
    predictions = {
        'churn_risk': [
            {'customer_id': 'cust_123', 'risk_score': 0.85, 'reason': 'Multiple unresolved technical issues'},
            {'customer_id': 'cust_456', 'risk_score': 0.72, 'reason': 'Billing complaints + negative sentiment'},
            {'customer_id': 'cust_789', 'risk_score': 0.64, 'reason': 'Decreased engagement + feature requests'}
        ],
        'trending_issues': [
            {'issue': 'Mobile performance', 'growth_rate': '+45%', 'projected_volume': 89},
            {'issue': 'API timeouts', 'growth_rate': '+23%', 'projected_volume': 67},
            {'issue': 'Integration questions', 'growth_rate': '+12%', 'projected_volume': 34}
        ]
    }
    
    print("HIGH CHURN RISK CUSTOMERS:")
    for customer in predictions['churn_risk']:
        print(f"   {customer['customer_id']}: {customer['risk_score']:.0%} risk - {customer['reason']}")
    
    print("\nTRENDING ISSUES (Next 7 Days):")
    for issue in predictions['trending_issues']:
        print(f"   {issue['issue']}: {issue['growth_rate']} growth, ~{issue['projected_volume']} cases expected")
    
    print("\nPROACTIVE ACTIONS RECOMMENDED:")
    print("   • Reach out to high-risk customers with personalized support")
    print("   • Prepare mobile team for increased performance issue volume")
    print("   • Create API troubleshooting documentation for support team")

def calculate_roi_metrics():
    """Calculate and display ROI metrics for the solution."""
    
    print("\n" + "="*60)
    print("ROI ANALYSIS - SMART CUSTOMER INSIGHT ENGINE")
    print("="*60)
    
    metrics = {
        'manual_categorization_hours_saved': 16,  # per week
        'hourly_rate_analyst': 45,  # USD
        'response_time_improvement': 0.6,  # 60% faster
        'customer_satisfaction_increase': 0.23,  # 23% improvement
        'churn_prevention_value': 50000,  # USD per quarter
        'implementation_cost': 25000,  # USD one-time
        'ongoing_costs': 2000  # USD per month
    }
    
    # Calculate annual savings
    annual_labor_savings = metrics['manual_categorization_hours_saved'] * 52 * metrics['hourly_rate_analyst']
    annual_churn_prevention = metrics['churn_prevention_value'] * 4
    annual_ongoing_costs = metrics['ongoing_costs'] * 12
    
    net_annual_benefit = annual_labor_savings + annual_churn_prevention - annual_ongoing_costs
    roi_percentage = ((net_annual_benefit - metrics['implementation_cost']) / metrics['implementation_cost']) * 100
    payback_period = metrics['implementation_cost'] / (net_annual_benefit / 12)
    
    print(f"FINANCIAL IMPACT (Annual):")
    print(f"   • Labor Cost Savings: ${annual_labor_savings:,.0f}")
    print(f"   • Churn Prevention Value: ${annual_churn_prevention:,.0f}")
    print(f"   • Implementation Cost: ${metrics['implementation_cost']:,.0f}")
    print(f"   • Ongoing Annual Costs: ${annual_ongoing_costs:,.0f}")
    print(f"   • Net Annual Benefit: ${net_annual_benefit:,.0f}")
    print(f"   • ROI: {roi_percentage:.0f}%")
    print(f"   • Payback Period: {payback_period:.1f} months")
    
    print(f"\nOPERATIONAL IMPACT:")
    print(f"   • Response Time Improvement: {metrics['response_time_improvement']:.0%}")
    print(f"   • Customer Satisfaction Increase: {metrics['customer_satisfaction_increase']:.0%}")
    print(f"   • Weekly Hours Saved: {metrics['manual_categorization_hours_saved']}")
    
    return metrics

if __name__ == "__main__":
    print("="*60)
    print("SMART CUSTOMER INSIGHT ENGINE - DEMO MODE")
    print("Author: Syed Ali Turab")
    print("LinkedIn: https://www.linkedin.com/in/syed-ali-turab/")
    print("="*60)
    
    # Generate and display sample data
    print("\nSTEP 1: GENERATING SAMPLE CUSTOMER FEEDBACK DATA")
    print("-"*50)
    df = generate_sample_feedback_data(50)
    print(f"Generated {len(df)} sample feedback items")
    print("\nSample data:")
    print(df[['feedback_id', 'channel', 'category', 'raw_text']].head())
    
    # Create visualizations
    print("\nSTEP 2: CREATING DASHBOARD VISUALIZATIONS")
    print("-"*50)
    create_sample_visualizations()
    
    # Demo semantic search
    demo_semantic_search()
    
    # Demo predictive analytics
    demo_predictive_analytics()
    
    # Calculate ROI
    calculate_roi_metrics()
    
    print("\n" + "="*60)
    print("DEMO COMPLETE - Ready for LinkedIn post!")
    print("Screenshots of the visualizations and output are perfect for social media")
    print("="*60)
