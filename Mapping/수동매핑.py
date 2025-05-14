# ────────────────────────────────
# 3. 수동 기준 매핑
# ────────────────────────────────
def unified_rule_based_mapping_food(name: str) -> str:
    name = str(name).replace(" ", "").replace("\n", "").lower()

    # 1. '탕'으로 끝나면 먼저 탕류에서 매칭
    if name.endswith("탕"):
        if any(k in name for k in ["삼계탕", "백숙", "반계탕","보신탕","옻계탕"]):
            return "삼계탕"
        if any(k in name for k in ["순대국", "설렁탕", "곰탕", "사골", "만두국", "만둣국", "해장국", "국밥", "설탕탕", "곰탐", "설농탕", "내장탕"]):
            return "설렁탕"
        if "갈비탕" in name:
            return "갈비탕"

    # 2. '차' 나 '티'로 끝나면 먼저 디저트에서 매칭
    if name.endswith("차" or "티"):
       #차
        if any(k in name for k in ["커피", "아메리카노", "라떼", "비엔나","아인슈페너"]):
            return "커피"
        if any(k in name for k in ["쌍화차", "다방커피"]):
            return "국산차"

    #3. 돈까스로 끝나면 먼저 돈가스로 매칭
       #일식
    if name.endswith("돈가스" or "돈까스" or "까스" or "카츠"):
        if any(k in name for k in ["돈가스", "돈까스", "까스", "카츠", "돈부리"]):
          return "돈가스"

    #4 탕수육으로 끝나면 탕수육ㅇ로 매칭
    if name.endswith("탕수육"):
        return "탕수육"

    if name.endswith("짬뽕" or "짬뽕밥"):
        return "짬뽕"

    #일식
    if any(k in name for k in ["돈가스", "돈까스", "까스", "카츠", "돈부리"]):
        return "돈가스"
    if any(k in name for k in ["초밥"]):
        return "생선초밥"

    #중식
    if any(k in name for k in ["탕수육","꿔바로우"]):
        return "탕수육"
    if any(k in name for k in ["간짜장","짜장면", "자장면", "짜장"]):
        return "자장면"
    if "짬뽕" in name:
        return "짬뽕"

    #탕류
    if any(k in name for k in ["삼계탕", "백숙","반계탕"]):
        return "삼계탕"
    if any(k in name for k in ["순대국", "설렁탕","곰탕", "사골", "만두국", "만둣국", "해장국", "국밥","설탕탕","곰탐","설농탕", "내장탕","추어탕","도가니탕"]):
        return "설렁탕"
    if any(k in name for k in ["갈비탕"]):
        return "갈비탕"

    #한식
    if any(k in name for k in ["냉면", "국수", "쫄면","모밀"]):
        return "냉면"
    if any(k in name for k in ["비빔밥", "쌈밥", "덮밥", "볶음밥", "백반", "솥밥", "알밥", "오믈렛", "오므라이스", "묵밥"]):
        return "비빔밥"
    if any(k in name for k in ["된장","된장찌개", "청국장"]):
        return "된장찌개백반"
    if any(k in name for k in ["고추장찌개","참치찌개","김치찌개","김치찜","김치찌개", "부대찌개", "순두부", "육개장"]):
        return "김치찌개백반"
    if "김밥" in name:
        return "김밥"

    # 고기류
    if any(k in name for k in ["뚝불","불고기", "석쇠불고기", "뚝배기불고기", "매운불고기", "간장불고기", "고추장불고기", "버섯불고기", "와규불고기", "양념불고기","제육","불백"]):
        return "불고기"
    if any(k in name for k in ["소고기", "살치살", "꽃등심", "등심", "안심", "토시살", "부채살", "제비추리", "업진살", "치마살", "와규"]):
        return "쇠고기(외식)"
    if any(k in name for k in ["돼지 숯불 갈비","돼지양념갈비","돼지갈비", "양념돼지갈비", "생돼지갈비", "갈비구이", "돼지왕갈비", "석쇠돼지갈비","갈비찜", "바베큐갈비"]):
        return "돼지갈비"
    if any(k in name for k in ["냉동삼겹살","냉삼","목살","삼겹","삼겹살", "생삼겹살", "오겹살", "항정살", "가브리살", "돼지목살", "껍데기", "마늘삼겹살", "양념삼겹살", "왕삼겹살", "숙성삼겹살", "수제삼겹살", "한돈삼겹살"]):
        return "삼겹살"

    #간식류
    if any(k in name for k in ["바비큐 구이","통닭","치킨", "후라이드", "순살", "닭강정"]):
        return "치킨"
    if any(k in name for k in ["피자","고르곤졸라","마르게리따","베이컨포테이토","하와이안","페페로니"]):
        return "피자"

    #면류
    if any(k in name for k in ["칼국수", "수제비","국시","칼제비"]):
        return "칼국수"
    if any(k in name for k in ["라면", "우동","라볶이"]):
        return "조리라면"

    #차
    if any(k in name for k in ["커피", "아메리카노", "라떼", "에이드", "비엔나"]):
        return "커피"
    if any(k in name for k in ["쌍화차", "다방커피"]):
        return "국산차"

    # 불가
    if any(k in name for k in ["추가","2인", "맥주", "소주", "참이슬", "별빛청하", "공기밥", "사리", "주류", '마사지',"콜라", "스프라이트", "생수", "육수", "사이다","후식","환타", "음료수", '소스','석박지','겉절이', '어린이', '사리' ]):
        return "불가"

    return None

def unified_rule_based_mapping_nonfood(name: str) -> str:
    name = str(name).replace(" ", "").replace("\n", "").lower()

    # 기타 서비스업
    if any(k in name for k in ["커트", "컷"]):
        return "미용료(커트)"
    if ("커트" in name or "컷" in name or "남자" in name):
        return "이용료(커트)"
    if ("파마" in name or "펌" in name):
        return "미용료(파마)"
    if any(k in name for k in ["양복", "드라이클리닝", "세탁"]):
        return "양복세탁료"
    if any(k in name for k in ["의복", "수선"]):
        return "의복수선료"
    if "당구" in name:
        return "당구장이용료"
    if "노래방" in name:
        return "노래방이용료"
    if any(k in name for k in ["pc", "피시방"]):
        return "PC방이용료"
    if any(k in name for k in ["사진", "촬영", "스튜디오", "명함"]):
        return "사진촬영료"
    if any(k in name for k in ["숙박", "여관", "모텔"]):
        return "숙박료(여관)"
    if any(k in name for k in ['대인', '때밀이', '성인', "목욕", "대중탕"]):
        return "목욕료"
    if any(k in name for k in ["찜질", '사우나']):
        return "찜질방이용료"

    #  불가
    if any(k in name for k in ["2인", '경로', '어린이', '소인', '초등', '아동', '회원권', '마사지', '쿠폰', '염색']):
        return "불가"

    return None

# ────────────────────────────────
# 4. 수동 기준 매핑 적용
# ────────────────────────────────
# food_all_menu.loc[:, "수동기준메뉴"] = food_all_menu["내용"].apply(unified_rule_based_mapping_food)
nonfood_menu.loc[:, "수동기준메뉴"] = nonfood_menu["내용"].apply(unified_rule_based_mapping_nonfood)
