nhập  cv2
nhập  numpy  dưới dạng  np
cap  =  cv2 . VideoCapture ( 'tromxe.webm' )
ret , frame1  =  cap . đọc ()
ret , frame2  =  cap . đọc ()
trong khi  nắp . isOpened ():
    khác  =  cv2 . absdiff ( frame1 , frame2 )
    xám  =  cv2 . cvtColor ( diff , cv2 . COLOR_BGR2GRAY )
    mờ  =  cv2 . GaussianBlur ( xám , ( 5 , 5 ), 0 )
    _ , thresh  =  cv2 . ngưỡng ( mờ , 20 , 255 , cv2 . THRESH_BINARY )
    giãn ra  =  cv2 . giãn ra ( đập lúa , Không , lặp đi lặp lại = 0 )
    đường viền , _  =  cv2 . findContours ( giãn ra , cv2 . RETR_TREE , cv2 . CHAIN_APPROX_SIMPLE )
    cho  đường viền  trong  đường viền :
        ( x , y , w , h ) =  cv2 . bindingRect ( đường viền )
        nếu  cv2 . contourArea ( đường viền ) <  800 :
            tiếp tục
        cv2 . hình chữ nhật ( frame1 , ( x , y ), ( x  +  w , y  +  h ), ( 0 , 255 , 0 ), 2 )
        cv2 . putText ( frame1 , 'Trạng thái: {}' . format ( 'Phát hiện chuyển động' ),
                    ( 10 , 20 ), cv2 . FONT_HERSHEY_SIMPLEX , 1 , ( 0 , 0 , 255 ), 3 )
    cv2 . imshow ( 'nguồn cấp dữ liệu phát hiện chuyển động' , frame1 )
    frame1  =  frame2
    ret , frame2  =  cap . đọc ()
    nếu  cv2 . waitKey ( 40 ) ==  ord ( "q" ):
        nghỉ
cv2 . killAllWindows ()
nắp . phát hành ()
