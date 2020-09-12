Public Class Item

    Public Enum eItemKind
        CONSUME = 501
        EQUIP
        MESSAGE
        EVENTGEN
        NEEDLESS
    End Enum

    Private pb As PictureBox
    Public Property pPB As PictureBox
        Get
            Return pb
        End Get
        Set(value As PictureBox)
            pb = value
        End Set
    End Property
    Private parentSlotNum As Integer
    Public Property pParentSlotnum As Integer
        Get
            Return parentSlotNum
        End Get
        Set(value As Integer)
            parentSlotNum = value
        End Set
    End Property

    Private itemKind As eItemKind
    Public Property pItemKind As eItemKind
        Get
            Return itemKind
        End Get
        Set(value As eItemKind)
            itemKind = value
        End Set
    End Property
    Private id As Integer
    Public Property pId As Integer
        Get
            Return id
        End Get
        Set(value As Integer)
            id = value
        End Set
    End Property
    Private name As String
    Public Property pName As String
        Get
            Return name
        End Get
        Set(value As String)
            name = value
        End Set
    End Property
    Private image As Image
    Public Property pImage As Image
        Get
            Return image
        End Get
        Set(value As Image)
            image = value
        End Set
    End Property
    Private iconName As String
    Public Property pIconName As String
        Get
            Return iconName
        End Get
        Set(value As String)
            iconName = value
        End Set
    End Property
    Private linkFormId As Integer
    Public Property pLinkFormId As Integer
        Get
            Return linkFormId
        End Get
        Set(value As Integer)
            linkFormId = value
        End Set
    End Property

    Private cursorImage As String
    Public Property pCursorImage As String
        Get
            Return cursorImage
        End Get
        Set(value As String)
            cursorImage = value
        End Set
    End Property

    Public Sub New(_id As Integer)
        id = _id
        Dim data As DataElement = Nothing
        If ItemData.GetInstance().FindElementByKey("Id", id, data) Then
            itemKind = CInt(data.DataIndexer("ItemKind").value)
            name = data.DataIndexer("Name").value
            iconName = data.DataIndexer("ItemImage").value
            linkFormId = CInt(data.DataIndexer("EventKind").value)
            cursorImage = data.DataIndexer("CursorImage").value
            image = GetResourceImage(iconName)

            pb = New PictureBox()
            pb.Image = image
            pb.SizeMode = PictureBoxSizeMode.StretchImage
            AddHandler pb.MouseDown, AddressOf Event_ItemInteraction
        End If
    End Sub

    Public Sub New(_itemKind As eItemKind, _id As Integer, _name As String,
                   Optional _image As Image = Nothing)
        itemKind = _itemKind
        id = _id
        name = _name
        image = _image

        pb = New PictureBox()
        pb.Image = image
        pb.SizeMode = PictureBoxSizeMode.StretchImage
        AddHandler pb.MouseDown, AddressOf Event_ItemInteraction
    End Sub

    Public Sub UseItem()
        Dim tempItem As Item = ItemContainer.GetInstance().GetItem(id)

        Select Case tempItem.itemKind
            Case eItemKind.CONSUME
                Inventory.GetInstance().RemoveItem(Me)
            Case eItemKind.EQUIP
                Dim cursor As Cursor = New Cursor(New IO.MemoryStream(CType(MainForm.rm.GetObject(cursorImage), Byte())))
                MainForm.Cursor = cursor
                MainForm.pUseItemId = tempItem.id
            Case eItemKind.MESSAGE
                Select Case Me.id
                    Case 102
                        MsgBox("주머니 속에 있던 꾸깃꾸깃한 쪽지에는 8이 써있다. 암호 .. 인 걸까?")
                        UIClass.GetInstance().pSafePassword(0).Visible = True
                    Case 104
                        If MsgBox("64 -> 63 -> 61 -> 57 -> 49 -> 33 -> ? .. 쪽지에 쓰여있는게 도대체 뭘까.",
                                  MsgBoxStyle.OkCancel) = MsgBoxResult.Ok Then
                            Dim answer As String = InputBox("답을 입력하세요.")

                            If answer = 1 Then
                                UIClass.GetInstance().pSafePassword(1).Visible = True
                                Inventory.GetInstance().RemoveItem(Me)
                            End If
                            UIClass.GetInstance().pQuestionBtn(0).Visible = True
                        End If
                End Select
                Inventory.GetInstance().RemoveItem(Me)
            Case eItemKind.EVENTGEN
                Select Case Me.linkFormId
                    Case 10003
                        MoleCatchingForm2.Show()
                End Select
            Case eItemKind.NEEDLESS
        End Select
    End Sub

    Public Sub Event_ItemInteraction(sender As Object, e As MouseEventArgs)
        If e.Button = MouseButtons.Left Then
            UseItem()
        End If
    End Sub
End Class
