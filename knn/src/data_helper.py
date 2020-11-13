import csv

with open('../data/Augmented_Iris.csv') as infile:
    reader = csv.DictReader(infile)
    with open('../data/iris.csv', 'w') as outfile:
        writer = csv.writer(outfile, delimiter=',')
        writer.writerow([
            'id', 'sepal_length_cm', 'sepal_width_cm', 'petal_length_cm', 'petal_width_cm', 'class'])
        cnt1 = 0
        cnt2 = 0
        cnt3 = 0
        cnt = 0
        for row in reader:
            if row['Species'] == 'Iris-setosa' and cnt1 < 5000:
                writer.writerow([
                    cnt, row['SepalLengthCm'], row['SepalWidthCm'],
                    row['PetalLengthCm'], row['PetalWidthCm'],
                    row['Species']])
                cnt1 += 1
                cnt += 1
            if row['Species'] == 'Iris-virginica' and cnt2 < 5000:
                writer.writerow([
                    cnt, row['SepalLengthCm'], row['SepalWidthCm'],
                    row['PetalLengthCm'], row['PetalWidthCm'],
                    row['Species']])
                cnt2 += 1
                cnt += 1
            if row['Species'] == 'Iris-versicolor' and cnt3 < 5000:
                writer.writerow([
                    cnt, row['SepalLengthCm'], row['SepalWidthCm'],
                    row['PetalLengthCm'], row['PetalWidthCm'],
                    row['Species']])
                cnt3 += 1
                cnt += 1