# Parcing vacancies

This Python project serves as a tool for gathering information about job vacancies from 2 the most popular platforms in Russia. The parser allows users to save collected data to a file and provides convenient functionalities for handling vacancies, including addition, filtering, and deletion.



### Data Collection

- Instantiate classes for working with job search APIs: `HeadHunterAPI` and `SuperJobAPI`.
- Retrieve vacancies from different platforms.



### User Interaction

- The `user_interaction` function enables interaction with the user via the console.
- Choose platforms, input search queries by salary, choose 3 actions:
- 1: delete vacancy 
- 2: add new vacancy
- 3: comparing salaries of 2 vacancies by their id 



## Parsing Platforms

1. **hh.ru:**
   - [HeadHunter API](https://github.com/hhru/api)

2. **superjob.ru:**
   - [SuperJob API](https://api.superjob.ru/)

## Data Output

- Job information is saved in a JSON file.
- Filtered and sorted vacancies are displayed to the user through the console.