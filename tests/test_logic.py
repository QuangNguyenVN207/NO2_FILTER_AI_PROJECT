# Kiểm thử (khuyến khích)

import pytest
def cong(a, b):
    return a+b

def test_cong():
    assert cong(2,3) == 5

#Trong Python, assert dùng để kiểm tra một điều kiện.
#👉 Nếu điều kiện đúng → chương trình chạy tiếp
#👉 Nếu điều kiện sai → chương trình báo lỗi ngay (AssertionError)

#Nói ngắn gọn: assert giúp phát hiện lỗi sớm.
# Cú pháp: assert điều_kiện, "Thông báo lỗi"