from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score

# Melakukan prediksi dengan model
y_pred = identify_face(faces)

# Membuat confusion matrix
cm = confusion_matrix(y_true, y_pred)

# Menghitung metrik evaluasi
accuracy = accuracy_score(y_true, y_pred)
precision = precision_score(y_true, y_pred, average='weighted')
recall = recall_score(y_true, y_pred, average='weighted')
f1 = f1_score(y_true, y_pred, average='weighted')

# Menampilkan hasil
print("Confusion Matrix:")
print(cm)
print(f"Accuracy: {accuracy}")
print(f"Precision: {precision}")
print(f"Recall: {recall}")
print(f"F1 Score: {f1}")
