#!/usr/bin/env python3
"""
Event Reminder Script - EventReminder Project
Uses requests==2.28.1 in its virtual environment
Fetches fake event data from JSONPlaceholder API
"""

import requests
import json

def fetch_event_data():
    """
    Fetch fake event data from JSONPlaceholder API
    
    Returns:
        dict: Event data or None if request fails
    """
    # JSONPlaceholder API endpoint for fake todo/event data
    url = "https://jsonplaceholder.typicode.com/todos/1"
    
    try:
        # Make API request using requests==2.28.1
        print(f"Using requests version: {requests.__version__}")
        response = requests.get(url, timeout=10)
        
        # Check if request was successful
        if response.status_code == 200:
            return response.json()
        else:
            print(f"❌ Error: Unable to fetch event data (Status code: {response.status_code})")
            return None
            
    except requests.exceptions.RequestException as e:
        print(f"❌ Network error: {e}")
        return None
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        return None

def display_event_reminder(event_data):
    """
    Display event reminder in a user-friendly format
    
    Args:
        event_data (dict): Event data from API
    """
    if not event_data:
        print("❌ Could not retrieve event data")
        return
    
    try:
        # Extract event information
        title = event_data.get('title', 'No title available')
        user_id = event_data.get('userId', 'Unknown')
        completed = event_data.get('completed', False)
        event_id = event_data.get('id', 'Unknown')
        
        # Display the main event reminder
        print(f"📅 Event Reminder: {title.title()}")
        
        # Additional event details
        status = "✅ Completed" if completed else "⏳ Pending"
        print(f"   Event ID: {event_id} | User: {user_id} | Status: {status}")
        
        # Show raw JSON data for learning purposes
        print(f"\n📋 Raw API Response:")
        print(json.dumps(event_data, indent=2))
        
    except Exception as e:
        print(f"❌ Error displaying event data: {e}")

def fetch_multiple_events(count=3):
    """
    Fetch multiple events for a more comprehensive demo
    
    Args:
        count (int): Number of events to fetch
    """
    print(f"\n🔍 Fetching {count} additional events...")
    
    events = []
    for i in range(1, count + 1):
        url = f"https://jsonplaceholder.typicode.com/todos/{i}"
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                events.append(response.json())
        except:
            continue
    
    if events:
        print(f"\n📋 Additional Events:")
        for i, event in enumerate(events, 1):
            status = "✅" if event.get('completed') else "⏳"
            print(f"   {i}. {status} {event.get('title', 'No title').title()}")

def main():
    """
    Main function - coordinates event fetching and display
    """
    print("=== EventReminder - Python Virtual Environment Demo ===")
    print("This script uses requests==2.28.1 from its virtual environment\n")
    
    try:
        # Fetch and display main event
        print("🔍 Fetching event reminder from JSONPlaceholder API...")
        event_data = fetch_event_data()
        display_event_reminder(event_data)
        
        # Ask user if they want to see more events
        try:
            show_more = input("\n❓ Would you like to see more events? (y/n): ").strip().lower()
            if show_more in ['y', 'yes']:
                fetch_multiple_events()
        except KeyboardInterrupt:
            pass
        
        print("\n✨ Event reminder check complete!")
        
    except KeyboardInterrupt:
        print("\n👋 Goodbye!")
    except Exception as e:
        print(f"❌ Unexpected error: {e}")

if __name__ == "__main__":
    main()