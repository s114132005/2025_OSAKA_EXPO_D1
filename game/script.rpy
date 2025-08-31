
# 圖片定義 (請根據你的照片檔名來修改)
image bg_taoyuan_airport_1 = "LINE_ALBUM_Test_250831_7.jpg"
image bg_taoyuan_airport_2 = "LINE_ALBUM_Test_250831_8.jpg"
image bg_taoyuan_airport_3 = "LINE_ALBUM_Test_250831_11.jpg"
image bg_taoyuan_airport_4 = "LINE_ALBUM_Test_250831_10.jpg"
image bg_taoyuan_airport_5 = "LINE_ALBUM_Test_250831_13.jpg"
image boarding_tw = Movie(play="movie/778312293_805608.webm")
image bg_taoyuan_airport_6 = "LINE_ALBUM_Test_250831_1.jpg"
image bg_airplane = "LINE_ALBUM_Test_250831_1.jpg"
#飛行途中
image plane_flying = Movie(play="movie/Img_4532.webm")
image plane_landing = Movie(play="movie/Img_4533.webm")

image bg_sky = "LINE_ALBUM_Test_250831_5.jpg"

#機場開始到藍天大廈以及飯店
# 1. 機場沒人, 2. 脈脈 3. 機場角落一側 4.早餐漢堡 5. 漢堡店窗外景色 ˊ6. 準備搭南海電鐵去大阪,到處都是萬博脈脈的廣告 7.南海電鐵的車是Hello kitty
# 8. 抵達大阪站,人山人海 9. 往梅田的方向走去,天氣很好,可以看到高聳的藍天大樓
image Kansai_1 = "LINE_ALBUM_Test_250831_5.jpg"
image Kansai_2 = "LINE_ALBUM_620_250830_58.jpg"
image Kansai_3 = "LINE_ALBUM_620_250830_57.jpg"
image hamburger_1 = "LINE_ALBUM_620_250830_56.jpg"
image hamburger_view = "LINE_ALBUM_Test_250901_1.jpg"
image haruka_1 = "LINE_ALBUM_Test_250831_2.jpg"
image haruka_2 = "LINE_ALBUM_620_250830_54.jpg"
image osaka_1 = "LINE_ALBUM_620_250830_42.jpg"
image osaka_2 = "LINE_ALBUM_620_250830_52.jpg"

label start:
    jump chapter_one_start # 跳轉到你的第一章腳本

label chapter_one_start:


    # 場景一：機捷
    scene bg_taoyuan_airport_1 with fade
    "（機場捷運的廣播聲）"
    "內心充滿了期待，這趟旅程，從桃園機場正式展開。"
       # 場景二:排隊check in
    scene bg_taoyuan_airport_2 with fade
    "雖然時間已經接近半夜，櫃檯前還是排滿了check in的人潮。"
    #場景三:空無一人的航廈
    scene bg_taoyuan_airport_3 with dissolve
    "因為是紅眼班機，接近登機時間的時候，航廈裡已經沒什麼人了。"

    #場景三:找到飛機，準備登機
    scene bg_taoyuan_airport_4 with fade
    "找到飛機了，這次搭樂桃，準備登機。"
    #場景三:找到飛機，準備登機
    scene bg_taoyuan_airport_5 with fade
    "這次搭的是登機門前面的位置，前面沒有坐人，腳可以伸直，不過遇到緊急情況的時候要協助空姐進行疏散。"

     # 顯示影片，並等待幾秒
    show boarding_tw with dissolve
    pause(5.0)  # 讓影片播放5秒，這裡可以調整時間長度

    # 在影片播放時，顯示旁白
    "第一次看到空橋脫離飛機。"

    # 等待玩家點擊，繼續播放影片
    # 如果你希望影片能繼續播放直到結束，可以使用一個較長的暫停時間，或者監聽影片結束的事件。
    # 最簡單的方法是使用 pause 來讓玩家控制節奏。
    pause

    "這真是個奇景。"

    # 當影片播放結束或劇情進入下一階段，將影片隱藏
    hide boarding_tw with dissolve

    #起飛
    scene bg_taoyuan_airport_6 with fade
    "飛機起飛，離開桃園機場。"
    #起飛
    scene bg_sky with fade
    "經過幾個小時的飛行，天亮了。"


    # 顯示第一段影片：飛機在空中飛行
    show plane_flying with dissolve
    "現在的高度可以清楚的看到海面上航行的船隻。"

    pause # 暫停，讓影片播放，等待玩家點擊繼續

    "經過了漫長的旅程，我們即將抵達目的地。"
    hide plane_flying with dissolve # 將影片淡出

    # 顯示第二段影片：飛機降落
    show plane_landing with dissolve
    "隨著機身緩緩下沉，地面上的建築物逐漸清晰。"
    
    pause # 再次暫停，讓降落影片播放，等待玩家點擊

    "機輪輕輕地碰觸到跑道，一陣微小的震動宣告了旅程的結束。"
    hide plane_landing with dissolve # 將影片淡出



# --- 機場沒人、脈脈、角落一側 ---
    scene Kansai_1 with fade
    "第一次踏上関西国際空港的土地，機場內人煙稀少，顯得格外寬敞寧靜。"

    scene Kansai_2 with dissolve
    "到處都看到了2025年大阪萬博的吉祥物脈脈(ミャクミャク)的廣告，感覺萬博的氛圍已經提前瀰漫開來了。"

    scene Kansai_3 with dissolve
    "在機場的角落，一個不起眼卻充滿故事感的地方，也拍下了這張照片。"
    
    scene Kansai_3 with dissolve
    "在機場的角落，一個不起眼卻充滿故事感的地方，也拍下了這張照片。"
    
    # --- 漢堡店選項 ---
    scene hamburger_1 with dissolve
    "肚子傳來一陣咕嚕聲..."
    "雖然剛下飛機，但感覺有點餓了，要不要先找個地方吃點東西再出發？"
    menu:
        "吃個漢堡當早餐":
            jump eat_hamburger_story

        "算了，直接去大阪市區吧！":
            jump skip_hamburger_story

label eat_hamburger_story:
    scene hamburger_1 with dissolve
    "我們找了間漢堡店，點了份熱騰騰的早餐。在異國的第一餐，感覺格外美味。"
    
    scene hamburger_view with dissolve
    "坐在靠窗的位置，一邊吃著漢堡，一邊欣賞著窗外的機場景色。"
    "吃飽喝足，我們準備前往大阪市區。"
    jump continue_to_osaka

label skip_hamburger_story:
    "雖然肚子有點餓，但還是決定將時間留給大阪市區的探索。"
    "事不宜遲，我們直接前往大阪車站。"
    jump continue_to_osaka

label continue_to_osaka:
    # --- 前往大阪市區 ---
    scene haruka_1 with fade
    "準備搭乘南海電鐵前往大阪，車站裡滿是萬博脈脈的宣傳廣告，提醒著我們大阪的熱情與活力。"

    scene haruka_2 with dissolve
    "更令人驚喜的是,我們搭上的是Hello Kitty主題列車!車廂內充滿了可愛的Hello Kitty元素,讓整個車程都變得超級夢幻。"

    scene osaka_1 with fade
    "抵達大阪車站，果然是人山人海，瞬間感受到大都市的喧囂與活力。"
    "（這裡可以加上你對大阪車站人潮的感想。）"

    scene osaka_2 with dissolve
    "我們往梅田的方向走去,今天天氣真好,遠遠地就看到了高聳的梅田スカイビル(Umeda Sky Building),準備前往這座充滿設計感的建築。"


    return
