# Quick Media Application

## Overview

This project is a Django-based social media aggregator that integrates with YouTube, Instagram, and Facebook. It provides a unified interface for users to interact with their social media content, leveraging the respective APIs to fetch and display data.

## Key features include

- **Unified Home Page**: Allows users to choose between YouTube, Instagram, or Facebook.

- **YouTube Integration**: Utilizes the YouTube API to fetch and store video data, displaying video content and player functionalities.

- **Instagram and Facebook Integration**: Employs custom models to mimic features like posts, likes, comments, and saves.

## Features

- **App Selection**: Users are prompted to select between YouTube, Instagram, or Facebook upon accessing the home page.

### YouTube Integration

- **API Utilization**: Fetches video data using the YouTube API.
- **Data Storage**: Stores fetched video data in the database for efficient future retrieval.
- **Video Display**: Shows video URLs and integrates a video player for viewing content.

### Instagram and Facebook Integration

- **Custom Models**: Creates custom Django models to simulate the functionalities of Instagram and Facebook.
- **Post Management**: Includes features for creating, liking, commenting, and saving posts.

## Technical Details

Backend Framework: Django
Database: PostgreSQL

### APIs Used

1. YouTube Data API
2. Custom Models & Implementation for Instagram and Facebook
3. Ajax Call for Crud

## Installation and Setup

- Clone Repository:

```bash
git clone [repository-url]
```

- Install Dependencies:

```bash
pip install -r requirements.txt
```

- Configure Settings:

Update `settings.py` with API keys and database configuration.

- Run Migrations:

```bash
python manage.py migrate
```

- Start Server:

```bash
python manage.py runserver
```

## Contributing

Feel free to submit issues, propose changes, or contribute directly through pull requests.

## License

This project is licensed under the MIT License.

Contact
For further information, please contact
