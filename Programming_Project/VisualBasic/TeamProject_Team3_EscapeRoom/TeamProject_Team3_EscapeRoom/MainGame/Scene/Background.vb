Public Class Background

    Public Enum eScrollDirection
        LEFT
        RIGHT
    End Enum

    Public Enum eBackground
        BG_BathRoom
        BG_BedRoom
        BG_MainRoom
        BG_Library
        BG_RoomBase
        QUANTITY
    End Enum

    Private isScroll As Boolean

    Private scrollDir As eScrollDirection
    Private scrollSpeed As Integer
    Private bgPB(GameScene.bgNum - 1) As PictureBox
    Public Property pBgPB(ByVal index As Integer) As PictureBox
        Get
            Return bgPB(index)
        End Get
        Set(value As PictureBox)
            bgPB(index) = value
        End Set
    End Property

    Private scrollBtn(1) As PictureBox

    Private tempGameScene As GameScene

    Public Sub Init()
        isScroll = False
        scrollDir = eScrollDirection.LEFT
        scrollSpeed = 80

        tempGameScene = SceneManager.GetInstance().GetSceneByKey("Game")

        SetBackground()
    End Sub

    Private Sub SetBackground()
        For i = 0 To UBound(bgPB)
            bgPB(i) = New PictureBox() With
            {
                .Width = MainForm.ClientSize.Width,
                .Height = MainForm.ClientSize.Height - MainForm.pUiPanel.Height,
                .BackgroundImageLayout = ImageLayout.Stretch
            }
            bgPB(i).Location = New Point(-(bgPB(i).Width * (tempGameScene.pMainBgNum)) + (bgPB(i).Width * i), 0)

            Dim resourceName As String = "bg" & (i + 1)
            bgPB(i).BackgroundImage = GetResourceImage(resourceName)

            MainForm.Controls.Add(bgPB(i))
            AddHandler bgPB(i).MouseDown, AddressOf Event_MouseDown
        Next

        ' ======================================= Scroll Button Temp Code
        scrollBtn(0) = New PictureBox() With
            {
                .Width = 50,
                .Height = 50,
                .BackColor = Color.Transparent,
                .Image = GetResourceImage("bgScrollButton_Left")
            }
        scrollBtn(0).Location = New Point(25, (MainForm.ClientSize.Height - scrollBtn(0).Height) / 2)
        'MainForm.Controls.Add(scrollBtn(0))
        bgPB(tempGameScene.pMainBgNum).Controls.Add(scrollBtn(0))
        scrollBtn(0).BringToFront()
        AddHandler scrollBtn(0).Click, AddressOf Event_LeftBtnClick
        AddHandler scrollBtn(0).MouseEnter, AddressOf Event_LeftBtnOver
        AddHandler scrollBtn(0).MouseLeave, AddressOf Event_LeftBtnLeave
        scrollBtn(1) = New PictureBox() With
            {
                .Width = 50,
                .Height = 50,
                .BackColor = Color.Transparent,
                .Image = GetResourceImage("bgScrollButton_Right")
            }
        scrollBtn(1).Location = New Point(MainForm.ClientSize.Width - scrollBtn(1).Width - 25, (MainForm.ClientSize.Height - scrollBtn(1).Height) / 2)
        'MainForm.Controls.Add(scrollBtn(1))
        bgPB(tempGameScene.pMainBgNum).Controls.Add(scrollBtn(1))
        scrollBtn(1).BringToFront()
        AddHandler scrollBtn(1).Click, AddressOf Event_RightBtnClick
        AddHandler scrollBtn(1).MouseEnter, AddressOf Event_RightBtnOver
        AddHandler scrollBtn(1).MouseLeave, AddressOf Event_RightBtnLeave
        ' ======================================= Scroll Button Temp Code
    End Sub

    Public Sub BG_KeyDown(e As KeyEventArgs)
        Select Case e.KeyCode
            Case Keys.Left
                Event_LeftBtnClick()
            Case Keys.Right
                Event_RightBtnClick()
        End Select
    End Sub

    Public Sub ChangeBG() ' Main Scene Num
        For i = 0 To UBound(bgPB)
            bgPB(i).Location = New Point(-(bgPB(i).Width * (tempGameScene.pMainBgNum)) + (bgPB(i).Width * i), 0)
        Next
        For i = 0 To UBound(scrollBtn)
            bgPB(tempGameScene.pMainBgNum).Controls.Add(scrollBtn(i))
            scrollBtn(i).BringToFront()
        Next
    End Sub

    Public Sub ChangeBG(sceneNum As Integer) ' Scene Num Parameter
        For i = 0 To UBound(bgPB)
            bgPB(i).Location = New Point(-(bgPB(i).Width * (sceneNum)) + (bgPB(i).Width * i), 0)
        Next
        For i = 0 To UBound(scrollBtn)
            bgPB(tempGameScene.pMainBgNum).Controls.Add(scrollBtn(i))
            scrollBtn(i).BringToFront()
        Next
    End Sub

    Public Sub ScrollBG() ' Main Scene Num
        If scrollDir = eScrollDirection.LEFT Then
            For i = 0 To UBound(bgPB)
                bgPB(i).Left += scrollSpeed
            Next
            If bgPB(tempGameScene.pMainBgNum).Location.X >= 0 Then
                ChangeBG()
                MainForm.ScrollTimer.Enabled = False
            End If
        Else
            For i = 0 To UBound(bgPB)
                bgPB(i).Left -= scrollSpeed
            Next
            If bgPB(tempGameScene.pMainBgNum).Location.X <= 0 Then
                ChangeBG()
                MainForm.ScrollTimer.Enabled = False
            End If
        End If
    End Sub

    Public Sub ScrollBG(sceneNum As Integer) ' Scene Num Parameter
        If scrollDir = eScrollDirection.LEFT Then
            For i = 0 To UBound(bgPB)
                bgPB(i).Left += scrollSpeed
            Next
            If bgPB(sceneNum).Location.X >= 0 Then
                ChangeBG(sceneNum)
                MainForm.ScrollTimer.Enabled = False
            End If
        Else
            For i = 0 To UBound(bgPB)
                bgPB(i).Left -= scrollSpeed
            Next
            If bgPB(sceneNum).Location.X <= 0 Then
                ChangeBG(sceneNum)
                MainForm.ScrollTimer.Enabled = False
            End If
        End If
    End Sub

    ' Use Item Cancel
    Public Sub Event_MouseDown(sender As Object, e As MouseEventArgs)
        If e.Button = MouseButtons.Right Then
            If MainForm.pUseItemId <> 0 Then
                MainForm.Cursor = Cursors.Arrow
                MainForm.pUseItemId = 0
                MsgBox("아이템 사용 취소.")
            End If
        End If
    End Sub

    ' Left Scroll
    Public Sub Event_LeftBtnClick()
        If isScroll Then
            If tempGameScene.pMainBgNum > 0 Then
                scrollDir = eScrollDirection.LEFT
                tempGameScene.pMainBgNum -= 1
                MainForm.ScrollTimer.Enabled = True
            End If
        Else
            If tempGameScene.pMainBgNum > 0 Then
                tempGameScene.pMainBgNum -= 1
                ChangeBG()
            End If
        End If
    End Sub

    ' Left Scroll Button Over
    Public Sub Event_LeftBtnOver()
        scrollBtn(0).Image = GetResourceImage("bgScrollButton_Left_over")
    End Sub

    ' Left Scroll Button Leave
    Public Sub Event_LeftBtnLeave()
        scrollBtn(0).Image = GetResourceImage("bgScrollButton_Left")
    End Sub

    ' Right Scroll
    Public Sub Event_RightBtnClick()
        If isScroll Then
            If tempGameScene.pMainBgNum < bgPB.Count - 1 Then
                scrollDir = eScrollDirection.RIGHT
                tempGameScene.pMainBgNum += 1
                MainForm.ScrollTimer.Enabled = True
            End If
        Else
            If tempGameScene.pMainBgNum < bgPB.Count - 1 Then
                tempGameScene.pMainBgNum += 1
                ChangeBG()
            End If
        End If
    End Sub

    ' Right Scroll Button Over
    Public Sub Event_RightBtnOver()
        scrollBtn(1).Image = GetResourceImage("bgScrollButton_Right_over")
    End Sub

    ' Right Scroll Button Leave
    Public Sub Event_RightBtnLeave()
        scrollBtn(1).Image = GetResourceImage("bgScrollButton_Right")
    End Sub
End Class
