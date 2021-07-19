# Project Plan for Code Challenge Tracker
This document exists to help me brainstorm and roadmap my project features. It's a preliminary document to help me organize my thoughts and capture my initial thinking. It also serves the my intention to learn in public; everyone can come to the GitHub repo and see how I went from project ideation to completion.

I fully expect over the course of the projec that things will change and that what I end up with will be different from what's outlined here.

## User Stories
If I had all of the time and talent in the world, I would implement the following stories. 

|   ID   | 	User Story             |
|  ----- | 	---------------------- |
|  S001  | 	I want to set a challenge start date.  |
|  S002  | 	I want to set a challenge duration. |
|  S003  | 	I want to know the end date of the challenge based on my start date. |
|  S004  | 	I want to know the current day of the challenge based on my start date. |
|  S005  | 	I want to know the remaining days left in the challenge based on my start date. |
|  S006  | 	I want to specify whether I completed or missed a challenge day. |
|  S007  | 	I want to know the total number of days that I missed. |
|  S008  | 	I want to adjust the end date of the challenge based on the number of days that I missed. |
|  S009  | 	I want to adjust the current day of the challenge based on the number of days that I missed. |
|  S010  | 	I want to adjust the remaining days left in the challenge based on the number of days that I missed. |
|  S011  | 	I want to know my longest streak of completed days. |
|  S012  | 	I want to know the longest streak of consecutive missed days. |
|  S013  | 	I want to set a limit on the number of missed days over a specified time-period. |
|  S014  | 	I want to be notified when I'm at risk of going over my missed day limit. |
|  S015  | 	I want to look up a challenge day based on a date that I enter. |
|  S016  | 	I want to look up a date based on a challenge day that I enter. |
|  S017  | 	I want to maintain a challenge journal. |
|  S018  | 	I want to create a journal entry for a challenge day. |
|  S019  | 	I want to modify a journal entry based on a date or challenge day that I specify. |
|  S020  | 	I want to delete a journal entry based on a date or challenge day that I specify. |
|  S021  | 	I want my journal to be version controlled. |
|  S022  | 	I want to see the full journal upon request. |
|  S023  | 	I want to export my journal from the tracker. |
|  S024  | 	I want to modify my start date. |

Since I'm short on time, I decided to organize the stories into an MVP (Minimum Viable Product) versus the nice-to-haves.

## MVP & Feature List
### MVP
When I originally came up with the idea of the code challenge tracker, my main motivation was to create something that could tell me the end date of the challenge and the current day that I was on based on my start date. I aligned the user stories into an MVP based on this initial motivation.

MVP List
|   ID   | 	User Story             |
|  ----- | 	---------------------- |
|  S001  | 	I want to set a challenge start date.  |
|  S002  | 	I want to set a challenge duration. |
|  S003  | 	I want to know the end date of the challenge based on my start date. |
|  S004  | 	I want to know the current day of the challenge based on my start date. |

The MVP is very basic, and although it doesn't seem all that exciting from a functionality standpoint, it's enough to test out and improve my current Python skills, which is ultimately what I hope to do by completing this project.

### Feature List
The MVP is a subset of a feature that I'm calling Progress Tracker. It is one of five main features that I came up with. Here's the full feature list:
|       Feature       | Description                                                               |
| ------------------- | ------------------------------------------------------------------------- |
| Progress Tracker    | Keeps track of your end date, current day, completed days and missed days |
| Progress Adjustment | Allows you to adjust end date & current day based on missed days          |
| Journal             | Create and manage a daily log of your accomplishments and thoughts        |
| Streaks             | View your longest streak of consecutive completed days and missed days    |
| Search              | Look up a challenge day by number or date                                 |

### Stories by Feature
The following sections list the stories by feature.

#### Progress Tracker

S001	I want to set a challenge start date. 
S002	I want to set a challenge duration.
S003	I want to know the end date of the challenge based on my start date.
S004	I want to know the current day of the challenge based on my start date.
S005	I want to know the remaining days left in the challenge based on my start date.
S006	I want to specify whether I completed or missed a challenge day.
S007	I want to know the total number of days that I missed.
S013	I want to set a limit on the number of missed days over a specified time-period.
S014	I want to be notified when I'm at risk of going over my missed day limit.

#### Progress Adjustment

S008	I want to adjust the end date of the challenge based on the number of days that I missed.
S009	I want to adjust the current day of the challenge based on the number of days that I missed.
S010	I want to adjust the remaining days left in the challenge based on the number of days that I missed.
S024	I want to modify my start date.

#### Journal

S017	I want to maintain a challenge journal.
S018	I want to create a journal entry for a challenge day.
S019	I want to modify a journal entry based on a date or challenge day that I specify.
S020	I want to delete a journal entry based on a date or challenge day that I specify.
S021	I want my journal to be version controlled.
S022	I want to see the full journal upon request.
S023	I want to export my journal from the tracker.

#### Streaks

S011	I want to know my longest streak of completed days.
S012	I want to know the longest streak of consecutive missed days.

#### Search

S015	I want to look up a challenge day based on a date that I enter.
S016	I want to look up a date based on a challenge day that I enter.