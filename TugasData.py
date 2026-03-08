import pandas as pd
import matplotlib.pyplot as plt

# membaca dataset
data = pd.read_csv("tips.csv")

# menghitung jumlah laki-laki dan perempuan
gender_count = data['sex'].value_counts()

# fungsi untuk menampilkan persentase + jumlah
def autopct_format(values):
    def my_format(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return f'{pct:.1f}%\n({val})'
    return my_format

# membuat pie chart
plt.figure(figsize=(6,6))

plt.pie(
    gender_count,
    labels=gender_count.index,
    autopct=autopct_format(gender_count),
    startangle=90
)

plt.title("Persentase Laki-laki dan Perempuan yang Memberikan Tips")

plt.show()