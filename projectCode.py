import pandas as pd
import logging

# Cấu hình logging
logging.basicConfig(
    filename="tmdb_analysis.log",  # Ghi log vào file
    level=logging.INFO,  # Mức độ ghi log (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format="%(asctime)s - %(levelname)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
)

# Đọc dữ liệu
data = pd.read_csv("tmdb-movies.csv")
logging.info("CSV file loaded successfully.")

# Hàm sửa lỗi năm
def fix_year(date):
    date = pd.to_datetime(date, format="%m/%d/%y", errors='coerce')
    if pd.notna(date):
        if date.year > 2025:
            return date.replace(year=date.year - 100)
        return date
    return date

data['release_date'] = data['release_date'].apply(fix_year)
logging.info("Fixed release_date format.")

# Chuyển đổi kiểu dữ liệu cho một số cột
col_to_convert = ['original_title', 'director', 'tagline', 'overview']
data[col_to_convert] = data[col_to_convert].astype(str)
logging.info("Converted columns to string type.")

# Sắp xếp theo ngày phát hành
df1 = data.sort_values(by='release_date', ascending=False)
df1.to_csv("sorted_by_date.csv", index=False)
logging.info("Sorted movies by release_date and saved to sorted_by_date.csv.")

# Lọc phim có đánh giá trung bình > 7.5
df2 = data[data['vote_average'] > 7.5]
df2.to_csv('filtered_by_vote_avg.csv', index=False)
logging.info(f"Filtered {len(df2)} movies with vote_average > 7.5 and saved to filtered_by_vote_avg.csv.")

# Tìm phim có doanh thu cao nhất và thấp nhất
max_revenue = data['revenue'].max()
min_revenue = data['revenue'].min()

df3 = data[data['revenue'] == max_revenue]
df4 = data[data['revenue'] == min_revenue]

logging.info(f"Movie with highest revenue: {df3[['original_title', 'revenue']].head(5)}")
logging.info(f"Movie with lowest revenue: {df4[['original_title', 'revenue']].head(5)}")

# Tổng doanh thu
sumRevenue = data['revenue'].sum()
logging.info(f"Total revenue of all movies: {sumRevenue}")

# Top 10 phim có doanh thu cao nhất
top10 = data.sort_values(by='revenue', ascending=False).head(10)
logging.info("Top 10 movies with highest revenue:")
logging.info(top10[['original_title', 'revenue']].to_dict())

# Đạo diễn có nhiều phim nhất
top1direct = data['director'].value_counts().idxmax()
logging.info(f"Director with most films: {top1direct}")

# Diễn viên đóng nhiều phim nhất
mostCast = data['cast'].str.split('|').explode().value_counts().idxmax()
logging.info(f"Actor with most films: {mostCast}")

# Thống kê số lượng phim theo thể loại
sortGenre = data['genres'].str.split('|').explode().value_counts()
logging.info("Top Genres:")
logging.info(sortGenre.to_dict())
