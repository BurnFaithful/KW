Public Class GameScene
    Inherits Scene

    Private bgInst As New Background

    Public Const bgNum As Integer = 5

    Private mainBgNum As Integer
    Public Property pMainBgNum As Integer
        Get
            Return mainBgNum
        End Get
        Set(value As Integer)
            mainBgNum = value
        End Set
    End Property

    Public Sub New(_name As String)
        MyBase.New(_name)
    End Sub

    Public Overrides Sub SetScene()

        mainBgNum = 1
        UIClass.GetInstance().SetUIPanel()
        bgInst.Init()
        DialogManager.GetInstance().Init()
        Inventory.GetInstance().Init()

        ' 프랍 생성
        ' 0 Bedroom, 1 Mainroom, 2 Passage, 3 Library, 4 Bathroom
        PropContainer.GetInstance().AddProp(bgInst.pBgPB(1), New Point(275, 350), 1) ' Drawer
        PropContainer.GetInstance().AddProp(bgInst.pBgPB(1), New Point(100, 400), 2) ' Bin
        PropContainer.GetInstance().AddProp(bgInst.pBgPB(1), New Point(300, 125), 3) ' TV
        PropContainer.GetInstance().AddProp(bgInst.pBgPB(0), New Point(165, 400), 9) ' Safe
        PropContainer.GetInstance().AddProp(bgInst.pBgPB(0), New Point(0, 0), 4) ' Closet
        PropContainer.GetInstance().AddProp(bgInst.pBgPB(4), New Point(450, 250), 7) ' Toilet
        PropContainer.GetInstance().AddProp(bgInst.pBgPB(2), New Point(300, 110), 6) ' Button Safe
        PropContainer.GetInstance().AddProp(bgInst.pBgPB(3), New Point(390, 220), 5) ' Desktop
        PropContainer.GetInstance().AddProp(bgInst.pBgPB(2), New Point(430, 120), 8) ' Toilet Door
        PropContainer.GetInstance().AddProp(bgInst.pBgPB(1), New Point(900, 95), 10) ' Exit Door
        ' ㅠㅠ ..

        PropContainer.GetInstance().GetProp(9).pPb.Visible = False
        ' ==================================== Item Property Set(Temp)
        Dim itemCount As Integer = DATA_ITEM_STARTNUM + ItemData.GetInstance().GetRowCount() - 1
        For i = DATA_ITEM_STARTNUM To itemCount
            ItemContainer.GetInstance().AddItem(i + 1)
        Next
        Inventory.GetInstance().AddItem(ItemContainer.GetInstance().GetItem(102))
        ' ==================================== Item Property Set(Temp)
    End Sub

    Public Overrides Sub KeyInput(e As KeyEventArgs)
        bgInst.BG_KeyDown(e)
    End Sub

    Public Overrides Sub Event_ScrollTimer_Tick()
        bgInst.ScrollBG(mainBgNum)
    End Sub

    Public Overrides Sub Event_DialogTimer_Tick()
        DialogManager.GetInstance().PrintDialog()
    End Sub
End Class
