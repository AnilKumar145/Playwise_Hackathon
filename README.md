# PlayWise Music Engine

A modular backend engine for personalized playlist management and instant music search, designed for education, hackathons, and scalable music platforms.

***

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Concepts & Data Structures](#concepts--data-structures)
- [Folder Structure](#folder-structure)
- [Getting Started](#getting-started)
- [How to Run (With VS Code or CLI)](#how-to-run-with-vs-code-or-cli)
- [Testing](#testing)
- [Author and License](#author-and-license)

***

## Project Overview

PlayWise helps users experience music like never before by combining data structures, algorithms, and clean code to deliver:

- Dynamic playlist management  
- Playback history and undo  
- Song rating and recommendations  
- Instant lookup by song ID or title (even on huge lists!)
- Time-based sorting with custom merge sort
- Performance optimization through complexity analysis
- Live system dashboard for debugging and monitoring

This repo is a teaching-grade demo of how core CS concepts can power real-world systems.

***

## Features

| Problem # | Feature                              | Core Functionality                                                                 |
|-----------|--------------------------------------|------------------------------------------------------------------------------------|
| 1         | Playlist Engine (Doubly Linked List) | Add, move, reverse, delete songs efficiently                                       |
| 2         | Playback History (Stack)             | Record playback order, allow undo/re-add last played song                          |
| 3         | Song Rating Tree (BST)               | Index/search/delete songs by rating; each rating = a bucket in binary search tree  |
| 4         | Instant Song Lookup (HashMap)        | O(1) retrieval of song by song ID or title; map is kept synced with playlist       |
| 5         | Time-based Sorting (Merge Sort)      | Sort playlists by title, duration, or recently added using custom merge sort       |
| 6         | Playback Optimization (Analysis)     | Annotate methods with time/space complexity; identify optimization opportunities   |
| 7         | System Snapshot Dashboard            | Live debugging interface showing top songs, recent plays, and rating distribution  |

***

## Concepts & Data Structures

- **Doubly Linked List:** Used for fast and flexible playlist operations.
- **Stack:** Supports undo in playback history (LIFO pattern).
- **Binary Search Tree (BST):** Bins songs into rating buckets (nodes), for O(log n) search by user rating.
- **Hash Map (dict):** Enables constant-time lookup by song ID or title—critical for scalable search.
- **Merge Sort:** Divide-and-conquer sorting algorithm with O(n log n) time complexity for flexible playlist ordering.
- **Complexity Analysis:** Time and space analysis for all core operations to ensure optimal performance.
- **System Integration:** Dashboard aggregates data from all modules using sorting, BST traversal, and hash map lookups.

All modules are extensible and use Python OOP best practices.

***

## Folder Structure

```
playwise_engine/
│
├── playlist/              # Problem 1: Playlist Engine modules
│   ├── playlist.py
│   ├── song.py
│   └── tests/
│
├── playback_history/      # Problem 2: Playback History Stack
│   ├── playback_controller.py
│   ├── playback_engine.py
│   ├── stack.py
│   └── tests/
│
├── song_rating_tree/      # Problem 3: Rating BST
│   ├── song_rating_engine.py
│   ├── rating_bst.py
│   ├── rating_bucket.py
│   └── tests/
│
├── song_lookup_map/       # Problem 4: HashMap Lookup
│   ├── lookup_map.py
│   └── tests/
│
├── playlist_sorting/      # Problem 5: Time-based Sorting
│   ├── sort_engine.py
│   └── tests/
│
├── system_dashboard/      # Problem 7: Live Dashboard
│   ├── dashboard.py
│   └── tests/
│
├── COMPLEXITY_ANALYSIS.md # Problem 6: Complexity documentation
├── main.py                # Master demonstration of all features
└── requirements.txt       # Install dependencies here
```

***

## Getting Started

### 1. Clone the Repository

```sh
git clone https://github.com/<your-username>/playwise_engine.git
cd playwise_engine
```

### 2. Set Up Your Virtual Environment

```sh
python -m venv venv
# On Windows
venv\Scripts\activate
# On Mac/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```sh
pip install -r requirements.txt
```

***

## How to Run (With VS Code or CLI)

From the root folder:

```sh
python main.py
```

- This runs an end-to-end demo covering all seven problems sequentially.
- Each module and feature prints its functionality—follow the on-screen output!
- The final dashboard displays live system statistics and exports JSON snapshot.

***

## Testing

Tests are written using Python's built-in `unittest` (and compatible with pytest).

To run all tests:
```sh
python -m unittest discover -s playlist/tests
python -m unittest discover -s playback_history/tests
python -m unittest discover -s song_rating_tree/tests
python -m unittest discover -s song_lookup_map/tests
python -m unittest discover -s playlist_sorting/tests
python -m unittest discover -s system_dashboard/tests
```

Or, to run ALL tests at once:
```sh
python -m unittest discover
```

***

## Dashboard Features

The System Snapshot Dashboard (Problem 7) provides:

- **System Overview:** Total songs, duration, average length, playback history count
- **Top 5 Longest Songs:** Sorted by duration using merge sort
- **Recently Played:** Last 5 songs from playback stack
- **Song Count by Rating:** Distribution using BST traversal
- **Extremes:** Shortest and longest songs in playlist
- **JSON Export:** Complete system snapshot for external analysis

Access the dashboard programmatically:
```python
from system_dashboard.dashboard import SystemDashboard

dashboard = SystemDashboard(playlist, playback_controller, rating_engine, lookup_map)
dashboard.print_dashboard()  # Pretty-printed console output
snapshot = dashboard.export_snapshot()  # JSON export
```

***

## Author and License

**Created by:** SALA ANIL KUMAR


***

## Contributing

Pull requests and improvements are welcome! This project serves as an educational resource for:
- Data Structures and Algorithms courses
- Hackathon preparation
- System design practice
- Performance optimization learning

