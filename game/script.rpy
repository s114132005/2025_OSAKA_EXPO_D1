# 圖片定義 (請根據你的照片檔名來修改)
image bg_taoyuan_airport_1 = "LINE_ALBUM_Test_250831_7.jpg"
image bg_taoyuan_airport_2 = "LINE_ALBUM_Test_250831_8.jpg"
image bg_taoyuan_airport_3 = "LINE_ALBUM_Test_250831_11.jpg"
image bg_taoyuan_airport_4 = "LINE_ALBUM_Test_250831_10.jpg"
image bg_taoyuan_airport_5 = "LINE_ALBUM_Test_250831_13.jpg"
image boarding_tw = Movie(play="movie/778312293_805608.webm",fit=True,loop=False)
image bg_taoyuan_airport_6 = "LINE_ALBUM_Test_250831_1.jpg"
image bg_airplane = "LINE_ALBUM_Test_250831_1.jpg"
#飛行途中
image plane_flying = Movie(play="movie/Img_4532.webm",loop=False)
image plane_landing = Movie(play="movie/Img_4533.webm",loop=False)

image bg_sky = "LINE_ALBUM_Test_250831_5.jpg"

#機場開始到藍天大廈以及飯店
# 1. 機場沒人, 2. 脈脈 3. 機場角落一側 4.早餐漢堡 5. 漢堡店窗外景色 ˊ6. 準備搭南海電鐵去大阪,到處都是萬博脈脈的廣告 7.南海電鐵的車是Hello kitty
# 8. 抵達大阪站,人山人海 9. 往梅田的方向走去,天氣很好,可以看到高聳的藍天大樓
image Kansai_1 = "LINE_ALBUM_Test_250831_3.jpg"
image Kansai_2 = "LINE_ALBUM_620_250830_58.jpg"
image Kansai_3 = "LINE_ALBUM_620_250830_57.jpg"
image hamburger_1 = "LINE_ALBUM_620_250830_56.jpg"
image hamburger_view = "LINE_ALBUM_Test_250901_1.jpg"
image haruka_1 = "LINE_ALBUM_Test_250831_2.jpg"
image haruka_2 = "LINE_ALBUM_620_250830_54.jpg"
image osaka_1 = "LINE_ALBUM_620_250830_42.jpg"
image osaka_2 = "LINE_ALBUM_620_250830_52.jpg"

#藍天大樓
#1. 從底下看藍天大樓,可以介紹一下藍天大樓的歷史 2. 準備上去藍天大樓 3. 從藍天大樓往下看的景色
#4. 可以在室內的咖啡廳喝咖啡 5. 點一杯咖啡看窗外的景色很愜意 6.可以在這邊看風景休息 7.也可以選擇到樓上的觀景台看風景
image Biru_1 = "LINE_ALBUM_620_250830_51.jpg"
image Biru_2 = "LINE_ALBUM_620_250830_50.jpg"
image Biru_3 = "LINE_ALBUM_Test_250901_2.jpg"
image Biru_4 = "LINE_ALBUM_Test_250901_3.jpg"
image Biru_5 = "LINE_ALBUM_620_250830_48.jpg"
image Biru_6 = "LINE_ALBUM_620_250830_49.jpg"
image Biru_7 = "LINE_ALBUM_620_250830_45.jpg"

#前往住宿+午餐+難波逛街+阿輩野
# 1.接下來回到大阪車站, 準備去這幾天住宿的地方 2. room tour
image hotel_1 = "LINE_ALBUM_620_250830_45.jpg"
image room_tour = Movie(play="movie/Video_566332449110622576_Qrblfkrw.webm",loop=False)
# 晚餐
image dinner_place = "LINE_ALBUM_Test_250831_1.jpg"
# 結局
image end_scene = "LINE_ALBUM_Test_250831_1.jpg"
# 世博
image bg_expo_main_hall = "LINE_ALBUM_Test_250831_1.jpg"
image japan_pavilion = "LINE_ALBUM_Test_250831_1.jpg"
image usa_pavilion = "LINE_ALBUM_Test_250831_1.jpg"
# 額外
image bg_osaka_castle = "LINE_ALBUM_Test_250831_1.jpg"
image bg_shinsekai = "LINE_ALBUM_Test_250831_1.jpg"
image bg_dotonbori = "LINE_ALBUM_Test_250831_1.jpg"

# 用來追蹤蒐集到的章數量
default stamps_collected = 0

# 用來存放玩家蒐集到的鑰匙
default keys = ["key_start"] # 預設給玩家一把起始鑰匙

default has_eaten_dinner = False

label start:
    jump chapter_one_start # 跳轉到你的第一章腳本

label chapter_one_start:
    play music "With_You_Everet_Almond.mp3" loop
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
    "位置在登機門附近，前面沒有坐人，腳可以伸直，不過遇到緊急情況的時候要協助空姐進行疏散。"
    scene black # 將背景切換成全黑
    # 顯示影片，並等待幾秒
    show boarding_tw with dissolve
    # 在影片播放時，顯示旁白
    "第一次看到空橋脫離飛機。"
   # pause  # 讓影片播放5秒，這裡可以調整時間長度

    # 當影片播放結束或劇情進入下一階段，將影片隱藏
    hide boarding_tw with dissolve

    #起飛
    scene bg_taoyuan_airport_6 with fade
    "飛機起飛，離開桃園機場。"
    #起飛
    scene bg_sky with fade
    "經過幾個小時的飛行，天亮了。"

    scene black # 將背景切換成全黑
    # 顯示第一段影片：飛機在空中飛行
    show plane_flying with dissolve
    "現在的高度可以清楚的看到海面上航行的船隻，經過了漫長的旅程，我們即將抵達目的地。"
    #pause

    hide plane_flying with dissolve # 將影片淡出
    
    scene black # 將背景切換成全黑
    # 顯示第二段影片：飛機降落
    show plane_landing with dissolve
    "隨著機身緩緩下沉，地面上的建築物逐漸清晰。"
    "機輪輕輕地碰觸到跑道，一陣微小的震動後，平安的降落了。"
    hide plane_landing with dissolve # 將影片淡出

# --- 機場沒人、脈脈、角落一側 ---
    scene Kansai_1 with fade
    "第一次踏上關西機場的土地，機場內人煙稀少，顯得格外寬敞寧靜。"

    scene Kansai_2 with dissolve
    "到處都看到了2025年大阪萬博的吉祥物脈脈(ミャクミャク)的廣告，感覺萬博的氛圍已經提前瀰漫開來了。"

    scene Kansai_3 with dissolve
    "安靜的機場角落，陽光溫柔地從圓形穹頂灑落，窗外是藍天與寬廣的停機坪，靜靜等待旅人的到來。"
    
    # --- 漢堡店選項 ---
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
    "準備搭乘南海電鐵前往大阪，車站裡滿是萬博脈脈的宣傳廣告，彷彿整個大阪都是萬博的展場。"

    scene haruka_2 with dissolve
    "更令人驚喜的是,我們搭上的是Hello Kitty主題列車!車廂內充滿了可愛的Hello Kitty元素,讓整個車程都變得超級夢幻。"

    scene osaka_1 with fade
    "抵達大阪車站，果然是人山人海，瞬間感受到這座關西大城的喧囂與活力。"

    scene osaka_2 with dissolve
    "我們往梅田的方向走去,今天天氣真好,遠遠地就看到了高聳的梅田スカイビル(Umeda Sky Building),準備前往這座充滿設計感的建築。"
    jump umeda_sky_building_story

label umeda_sky_building_story:

    # 1. 從底下看藍天大樓，可以介紹一下藍天大樓的歷史
    scene Biru_1 with fade
    "一到達梅田スカイビル（Umeda Sky Building）樓下，就立刻被這棟獨特的建築所吸引。"
    "這座雙子塔建築，以其頂部連接的圓形空中庭園而聞名。"
    "它不只是大阪的地標，更被英國的雜誌評選為世界前二十名的建築物之一。"
    "抬頭仰望，那種充滿未來感的設計，讓人忍不住想要一探究竟。"
    
    # 2. 準備上去藍天大樓
    scene Biru_2 with dissolve
    "（這裡可以描述一下前往電梯的過程，或是排隊的人潮。）"
    "我們搭乘了高速電梯，只花了幾秒鐘就上升到了高處，然後再轉乘一段手扶梯，終於抵達了空中庭園展望台。"

    # 3. 從藍天大樓往下看的景色
    scene Biru_3 with dissolve
    "從高處俯瞰，整個大阪市區盡收眼底。"
    "高樓大廈、車水馬龍的街道，一切都變得好小，好像一個巨大的模型。"
    "遠處的淀川，像一條銀色的絲帶蜿蜒穿過城市，景色非常壯觀。"
    
    scene Biru_4 with dissolve
    "（這裡可以描述你對這個景色的感想。）"
    "這個高度和視角，與在地面完全不同，感覺自己好像站在雲端，看著整個城市在腳下運轉。"

    # 4. 可以在室內的咖啡廳喝咖啡
    menu:
        "到室內的咖啡廳休息一下。":
            jump cafe_story

        "直接到戶外觀景台看風景！":
            jump observation_deck_story

label cafe_story:
    # 5. 點一杯咖啡看窗外的景色很愜意
    scene Biru_5 with dissolve
    "我們選擇了在室內的咖啡廳坐下來，點了一杯熱騰騰的咖啡。"
    "（這裡可以加上你點的咖啡或甜點的描述。）"
    
    scene Biru_6 with dissolve
    "坐在舒適的沙發上，一邊品嚐著咖啡，一邊透過巨大的玻璃窗欣賞著窗外的景色。"
    "這份寧靜和愜意，讓剛剛在戶外的喧囂都沉澱了下來，感覺格外放鬆。"
    jump after_cafe_story

label observation_deck_story:
    # 6. 可以在這邊看風景休息
    scene Biru_7 with dissolve
    "我們直接走向戶外，這裡的視野更加遼闊，完全沒有玻璃的阻隔。"
    "（這裡可以加上風吹拂的感覺，或是更貼近天空的感覺。）"
    "迎面吹來的風，帶著城市特有的氣息，讓人感覺與這片景色融為一體。"
    "雖然戶外有點冷，但眼前的景色值得我們在這裡多停留一會兒。"
    
    jump after_cafe_story

label after_cafe_story:
    # 7.也可以選擇到樓上的觀景台看風景
    scene Biru_7 with dissolve
    "（這裡可以加上從咖啡廳出來後，前往戶外觀景台的轉折語氣。）"
    "喝完咖啡，我們也決定走到戶外的觀景台，體驗沒有玻璃阻隔的景色。"
    "迎面吹來的風，帶著城市特有的氣息，讓人感覺與這片景色融為一體。"
    "雖然戶外有點冷，但眼前的景色值得我們在這裡多停留一會兒。"

    "（這裡可以加上你對藍天大樓這個行程的總結。）"
    jump hotel

label hotel:
    scene osaka_1 with dissolve
    "逛完藍天大樓的觀景台後，準備要前往這幾天的住宿，在心齋橋附近。"
    # 顯示影片，並等待幾秒
    scene black # 將背景切換成全黑
    show room_tour with dissolve
    pause(3.0)  # 讓影片播放5秒，這裡可以調整時間長度

    # 在影片播放時，顯示旁白
    "帶大家來看看這幾天的住宿"

    # 等待玩家點擊，繼續播放影片
    # 如果你希望影片能繼續播放直到結束，可以使用一個較長的暫停時間，或者監聽影片結束的事件。
    # 最簡單的方法是使用 pause 來讓玩家控制節奏。
    pause

    "房間看起來很寬敞，缺點是窗戶看不到外面。"

    # 當影片播放結束或劇情進入下一階段，將影片隱藏
    hide room_tour with dissolve
    "你在入住後，準備開始探索這個城市。"

    "你計畫先去哪裡呢？"

    menu:
        "在飯店休息":
            jump rest_at_hotel

        "心齋橋逛街":
            jump shopping_at_shinsaibashi

        "阿倍野觀景台":
            jump visit_abenoharukas

        "新世界":
            jump explore_shinsekai

label rest_at_hotel:
    "你決定在舒適的飯店房間裡放鬆一下，為接下來的行程儲備體力。"
    "（這是關於在飯店休息的故事...）"
    jump to_dinner_story

label shopping_at_shinsaibashi:
    "你興奮地前往熱鬧的心齋橋，準備大肆採購一番。"
    "（這是關於心齋橋逛街的故事...）"
    jump to_dinner_story

label visit_abenoharukas:
    "你搭車前往阿倍野，從高處欣賞大阪的日落美景。"
    "（這是關於阿倍野觀景台的故事...）"
    jump to_dinner_story

label explore_shinsekai:
    "你來到充滿復古氛圍的新世界，感受歷史與美食的交織。"
    "（這是關於新世界的故事...）"
    jump to_dinner_story

label to_dinner_story:
    scene dinner_place with fade
    "結束了一天的行程，你的肚子發出了抗議聲。"
    "你決定去附近的一家餐廳，好好犒賞自己一番。"
    "（在這裡，你可以接續晚餐的劇情...）"
    menu:
        "直接回飯店休息":
            jump go_back_to_hotel_and_end_day
        
        "去道頓堀逛逛":
            jump explore_dotonbori_and_end_day
        
label go_back_to_hotel_and_end_day:
    "酒足飯飽後，你回到飯店，洗完澡後直接倒頭就睡。"
    "（這是關於回飯店睡覺的故事...）"
    "（你準備迎接全新的一天...）"
    jump day_two_osaka_castle

label explore_dotonbori_and_end_day:
    scene bg_dotonbori with fade
    "夜幕低垂，你來到燈火通明的道頓堀，準備感受大阪的夜生活。"
    "（這是關於道頓堀逛街的故事...）"
    "（你準備迎接全新的一天...）"
    jump day_two_osaka_castle

# 第二天的故事
label day_two_osaka_castle:
    scene bg_osaka_castle with fade
    "隔天早上，你精神飽滿地醒來，決定前往宏偉的大阪城。"
    "（這是關於大阪城的故事...）"
    "逛完大阪城後，你再次感到飢餓。"
    # 故事結束後，自動跳轉回晚餐標籤
    jump to_dinner_story

# 第三天的故事 - 萬博世博會
label day_three_expo:
    scene bg_expo_main_hall with fade
    "第三天，你來到了 2025 大阪世博會的主場館。"
    "你目前蒐集到 [stamps_collected] 個章。"
    "（你可以從這裡開始你新的世博會探索劇情。）"

if stamps_collected >= 5 and not has_eaten_dinner:
    "你已經逛了很久，肚子有點餓了，要不要去吃晚餐？"
    menu:
        "去吃晚餐":
            $ has_eaten_dinner = True
            jump to_dinner_story
        "繼續逛":
            "你決定繼續探索，直到肚子真的受不了為止。"
            $ has_eaten_dinner = True  # 設定為已看到提示，避免下次再彈出
            jump day_three_expo

    if stamps_collected == 20:
        "恭喜你，已經蒐集齊了所有章！"
        "你感到肚子有點餓了..."
        jump to_dinner_story

menu:
    "日本館" if "key_start" in keys:
        jump japan_pavilion
    "？？？" if "key_start" not in keys:
        pass

    "美國館" if "key_usa" in keys:
        jump usa_pavilion
    "？？？" if "key_usa" not in keys:
        pass

    # 你可以依此類推，為其他展館新增選項
    # "法國館" if "key_france" in keys:
    #     jump france_pavilion
    # "？？？" if "key_france" not in keys:
    #     pass

    # 或是加入其他通用選項
    "回到飯店休息":
        jump go_back_to_hotel

label japan_pavilion:
    scene japan_pavilion with fade
    "你進入了日本館，感受到了濃厚的科技與傳統交融的氛圍。"
    "（這裡可以加入日本館的劇情...）"
    
    # 玩家得到章和下一站的鑰匙
    $ stamps_collected += 1
    $ keys.append("key_usa") # 給予下一站的鑰匙
    
    "你得到了一枚精美的日本館紀念章！"
    "在出口處，你發現了一張神秘的紙條，上面寫著：『前往美國館，那裡有你需要的一切。』"
    "你將紙條收好，準備前往下一站。"
    jump day_three_expo

label usa_pavilion:
    scene usa_pavilion with fade
    "你來到了美國館，這裡充滿了未來感與創新科技。"
    "（這裡可以加入美國館的劇情...）"

    # 玩家得到章和下一站的鑰匙
    $ stamps_collected += 1
    $ keys.append("key_china") # 假設下一站是中國館
    
    "你得到了一枚充滿太空風格的美國館紀念章！"
    "館內的一台機器人對你說：『我們的旅程將帶你到東方。』"
    "你明白了它的提示，準備前往下一站。"
    jump day_three_expo

label go_back_to_hotel:
    "你在世博會逛累了，決定先回飯店休息。"
    "（這裡可以加入回飯店的劇情...)"
    "你決定明天再繼續。"
    jump day_three_expo

# 遊戲結局標籤
label the_end_label:
    scene end_scene with fade # 請自行替換為結局的背景圖
    "你成功蒐集了所有的章，這趟旅程圓滿結束！"
    "你帶著滿滿的回憶踏上歸途。"
    return
