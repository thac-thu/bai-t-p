nhập  cv2
nhập  mediapipe  dưới dạng  mp
 thời gian nhập khẩu
class  handDetector ():
    def  __init__ ( tự , chế độ = False , maxHands = 2 , detectionCon = 0,5 , trackCon = 0,5 ):
        bản thân . mode  =  chế độ
        bản thân . maxHands  =  maxHands
        bản thân . DiscoveryCon  =  phát hiện
        bản thân . trackCon  =  trackCon
        bản thân . mpHands  =  mp . các giải pháp . tay
        bản thân . tay  =  tự . mpHands . Tay ( tự . Chế độ , tự . MaxHands ,
                                        bản thân . phát hiệnCon , bản thân . trackCon )
        bản thân . mpDraw  =  mp . các giải pháp . draw_utils
    def  findHands ( self , img , draw = True ):
        imgRGB  =  cv2 . cvtColor ( img , cv2 . COLOR_BGR2RGB )
        bản thân . kết quả  =  bản thân . bàn tay . quy trình ( imgRGB )
        # print (results.multi_hand_landmarks)
        nếu  tự . kết quả . multi_hand_landmarks :
            cho  handLms  trong  tự . kết quả . multi_hand_landmarks :
                nếu  vẽ :
                    bản thân . mpDraw . draw_landmarks ( img , handLms ,
                                               bản thân . mpHands . HAND_CONNECTIONS )
        trả lại  img
    def  findPosition ( self , img , handNo = 0 , draw = True ):
        lmList  = []
        nếu  tự . kết quả . multi_hand_landmarks :
            myHand  =  tự . kết quả . multi_hand_landmarks [ handNo ]
            cho  id , lm  trong  liệt kê ( myHand . mốc ):
                # print (id, lm)
                h , w , c  =  img . hình dạng
                cx , cy  =  int ( lm . x  *  w ), int ( lm . y  *  h )
                # print (id, cx, cy)
                lmList . nối thêm ([ id , cx , cy ])
                nếu  vẽ :
                    cv2 . vòng tròn ( img , ( cx , cy ), 8 , ( 255 , 0 , 0 ), cv2 . FILLED )
        trả lại  lmList
def  main ():
    pTime  =  0
    cTime  =  0
    cap  =  cv2 . VideoCapture ( 0 )
    detector  =  handDetector ()
    trong khi  Đúng :
        thành công , img  =  cap . đọc ()
        img  =  máy dò . findHands ( img )
        lmList  =  máy dò . findPosition ( img )
        if  len ( lmList ) ! =  0 :
            in ( lmList [ 4 ])
        cTime  =  thời gian . thời gian ()
        fps  =  1  / ( cTime  -  pTime )
        pTime  =  cTime
        cv2 . putText ( img , f'toan: { int ( fps ) } ' , ( 10 , 70 ), cv2 . FONT_HERSHEY_PLAIN , 3 ,
                    ( 255 , 255 , 255 ), 3 )
        cv2 . putText ( img , 'toan pro' , ( 540 , 370 ), cv2 . FONT_HERSHEY_PLAIN , 1.5 ,
                    ( 0 , 255 , 255 ), 3 )
        cv2 . imshow ( "Hình ảnh" , img )
        cv2 . WaitKey ( 1 )
nếu  __name__  ==  "__main__" :
    main ()