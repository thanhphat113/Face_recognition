from unidecode import unidecode
name = "Nguyễn Văn X"

# Chuẩn hóa tên
normalized_name = unidecode(name).lower().replace(" ", "")

print(normalized_name)  # In ra: nguyenvanx