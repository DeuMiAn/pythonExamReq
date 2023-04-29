books = [
    {"제목": "안드로이드앱개발", "저자": "최전산", "출판사": "PCB", "가격": 25000, "출판연도": 2017},
    {"제목": "파이썬", "저자": "강수라", "출판사": "연두", "가격": 22000, "출판연도": 2019},
    {"제목": "자바스크립트", "저자": "박정식", "출판사": "SSS", "가격": 23000, "출판연도": 2018},
    {"제목": "HTML5", "저자": "주환", "출판사": "대한", "가격": 27500, "출판연도": 2012},
    {"제목": "컴파일러", "저자": "장진웅", "출판사": "PCB", "가격": 19500, "출판연도": 2011},
    {"제목": "C언어", "저자": "홍말숙", "출판사": "한국", "가격": 22000, "출판연도": 2010},
    {"제목": "프로그래밍언어", "저자": "현정숙", "출판사": "연두", "가격": 15000, "출판연도": 2019},
]

#화면에 도서 출력함수
def print_book(book):
    #Book 아이템을 제목, 저자, 출한사, 가격 순으로 print해주는 함수
    print("제목 : " + book["제목"])
    print("저자 : " + book["저자"])
    print("출판사 : " + book["출판사"])
    print("가격 : " + str(book["가격"])+"\n")

#전체 도서 리스트 출력함수
def print_book_list(books):
    #Books에 저장된 데이터 리스트를 for문으로 하나씩 print_book()함수로 print하는 함수
    for book in books:
        print_book(book)

#도서추가
def add_book(books):
    # 도서 정보를 입력받는다. 예외가 발생하면 다시 입력 받도록 한다.
    while True:
        try: 
            print("추가할 도서정보를 입력하세요. (제목 저자 출판사 가격 출판연도)")
            #input으로 입력받을때 공백 간격으로 입력받아 배열로 변환해줌[제목, 저자, 출판사,가격,출판연도]
            book_info = input(">> ").split()
            title, author, publisher, price, year = book_info
            price = int(price)
            year = int(year)
            book = {"제목": title, "저자": author, "출판사": publisher, "가격": price, "출판연도": year}
            break
        except:
            print("잘못된 입력입니다.")
    books.append(book)

    print("도서가 추가되었습니다.\n")
    print_book_list(books)

# 도서 키워드 선택 함수
def select_keyword():
    # 도서 정보를 입력받는다. 예외가 발생하면 다시 입력 받도록 한다.
    while True:
        try:
            print("검색키워드(도서명:1, 저자명:2, 출판사명:3, 출판연도:4) : ")
            keyword_choice = input()
            search_word = input(f"{['도서명', '저자명', '출판사', '출판연도'][int(keyword_choice)-1]} >> ")
            break
        except:
            print("잘못된 입력입니다.")
    return ['제목', '저자', '출판사','출판연도'][int(keyword_choice)-1], search_word


# 도서 검색 함수
def search_books(books, keyword, value):
    result_books = []
    for book in books:
        if str(book[keyword]) == str(value):
           
            result_books.append(book)
    if len(result_books) == 0:
        print("검색 결과가 없습니다.")
    else:
        print("\n===== 검색 결과 =====")
        for book in result_books:
            print_book(book)

#도서삭제함수
def delete_book(books):
    # 도서 정보를 입력받는다. 예외가 발생하면 다시 입력 받도록 한다.
    while True:
        try:
            print("삭제할 도서명과 저자명 입력하세요. (도서명 저자명)")
            title, author = input(">> ").split()
            break
        except:
            print("잘못된 입력입니다.")
    for book in books:
        if book["제목"] == title and book["저자"] == author:
            books.remove(book)

    print("도서가 삭제되었습니다.\n")
    print_book_list(books)


while True:
    print("="*70)
    print("입력값")
    print("1. 도서추가")
    print("2. 도서검색")
    print("    ∙도서명")
    print("    ∙저자명")
    print("    ∙출판사명")
    print("3. 도서삭제")
    print("4. 종료")
    choice = input("\n선택(1,2,3,4) : ")
    
    if choice == '1':
        add_book(books)
    elif choice == '2':
        keyword, value=select_keyword()
        search_books(books, keyword, value)
    elif choice =='3':
        delete_book(books)
    elif choice =='4':
        quit()