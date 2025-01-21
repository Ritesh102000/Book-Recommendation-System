# Book-Recommendation-System


This project processes and analyzes book rating data using Python's `pandas` library. The main objective is to filter and process large book-rating datasets to identify users and books that meet certain rating thresholds. The project then creates a pivot table to provide a matrix of user ratings for books that meet the specified criteria.

## Files Involved
- **Books.csv**: Contains book metadata (e.g., ISBN, title, author, publisher, image URLs).
- **Ratings.csv**: Contains ratings for books, including user IDs, ISBN, and rating score.
- **Users.csv**: Contains information about users, though not directly used in the analysis.

## Steps Involved

1. **Loading Data:**
   - Three CSV files (`Books.csv`, `Ratings.csv`, and `Users.csv`) are loaded into `pandas` dataframes.
   - The warning for mixed types in the columns is acknowledged, and the data is read despite the issue.

2. **Data Merging:**
   - The `Ratings.csv` file is merged with the `Books.csv` based on the ISBN of the books to create a combined dataframe (`book_rating`), which now contains book details along with ratings from users.

3. **Filtering Users with High Rating Activity:**
   - The data is grouped by `User-ID` to calculate the total sum of ratings by each user.
   - Users who have a total rating sum greater than 200 are selected for further analysis. These users are assumed to have significant rating activity.

4. **Filtering Books with High Rating Activity:**
   - The data is grouped by `Book-Title` to calculate the total sum of ratings for each book.
   - Books with a rating sum greater than 50 are retained. These books are assumed to have been rated a sufficient number of times to be of significant interest.

5. **Creating a Filtered Rating Dataset:**
   - A new filtered dataset is created that contains only ratings for users who have rated more than 200 books and for books that have been rated more than 50 times.
   - This dataset (`book_rating_new`) represents the most active users and popular books.

6. **Pivot Table Creation:**
   - The filtered dataset is then converted into a pivot table, where each row represents a book, each column represents a user, and the values represent the ratings given by users to those books.
   - The pivot table is created using the `pandas.pivot_table()` function, with missing ratings filled with zeroes.

## Functions

- **make_table(limit_user, limit_book, df)**:
  - This function processes the dataset to filter users and books based on the specified rating thresholds (`limit_user` and `limit_book`).
  - It groups the dataset by `User-ID` and `Book-Title` to filter and retain users who have rated more than the `limit_user` and books rated more than the `limit_book`.
  - It then returns a pivot table with the filtered data.

## Output

The final output is a pivot table, which is a matrix showing the ratings by active users (those who have rated more than 200 books) for popular books (those rated more than 50 times). Each row corresponds to a book and each column to a user.

## Example Output Format:

This table provides a user-by-book matrix with ratings, helping identify which users rated which books.

## Dependencies
- `pandas`: For data manipulation and analysis.

## Usage

1. Ensure you have the required CSV files (`Books.csv`, `Ratings.csv`, and `Users.csv`).
2. Run the Python script to generate the pivot table based on the specified filters.
3. Analyze the resulting pivot table to understand user-book interactions.


