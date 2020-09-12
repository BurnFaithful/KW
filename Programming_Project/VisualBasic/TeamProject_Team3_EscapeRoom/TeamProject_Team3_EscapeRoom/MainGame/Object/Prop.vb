Public Class Prop

    Private id As Integer
    Public ReadOnly Property pId As Integer
        Get
            Return id
        End Get
    End Property
    Private name As String
    Private resourceName As String
    Public Property pResourceName As String
        Get
            Return resourceName
        End Get
        Set(value As String)
            resourceName = value
        End Set
    End Property

    Private sndResourceName As String
    Public Property pSndResourceName As String
        Get
            Return sndResourceName
        End Get
        Set(value As String)
            sndResourceName = value
        End Set
    End Property

    Private isOpen As Boolean

    Private pb As PictureBox
    Public ReadOnly Property pPb As PictureBox
        Get
            Return pb
        End Get
    End Property

    Private linkEvent As New GameEvent
    Private linkItemId As Integer
    Public ReadOnly Property pLinkItemId As Integer
        Get
            Return linkItemId
        End Get
    End Property
    Private linkHiddenItemId As Integer
    Public ReadOnly Property pLinkHiddenItemId As Integer
        Get
            Return linkHiddenItemId
        End Get
    End Property
    Private linkDialogId As Integer
    Public ReadOnly Property pLinkDialogId As Integer
        Get
            Return linkDialogId
        End Get
    End Property
    Private linkFormId As Integer
    Public ReadOnly Property pLinkFormId As Integer
        Get
            Return linkFormId
        End Get
    End Property
    Private passRequirement As Integer
    Public ReadOnly Property pPassRequirement As Integer
        Get
            Return passRequirement
        End Get
    End Property

    Private collider As Button
    Private dialogMgrInst As DialogManager = DialogManager.GetInstance()

    Public Sub Init(parent As Control, pos As Point, _id As Integer)
        Static propNumber As Integer

        collider = New Button()
        collider.Name = "Prop" & propNumber & "Btn"
        MainForm.Controls.Add(collider)

        pb = New PictureBox()
        pb.Location = pos
        pb.BackColor = Color.Transparent
        parent.Controls.Add(pb)
        AddHandler pb.MouseDown, AddressOf Event_ClickEvent

        SubstituteParsingData(_id)

        pb.Name = name
        pb.Image = GetResourceImage(resourceName)
    End Sub ' Transparency + Definite Position + Event Id set-up(Parsing Data Substitution) Init

    Public Sub Event_ClickEvent(sender As Object, e As MouseEventArgs)
        Dim tempPB As PictureBox = CType(sender, PictureBox)

        ' 왼쪽 클릭
        If e.Button = MouseButtons.Left Then
            Dim tempProp As Prop = PropContainer.GetInstance().GetProp(tempPB)

            If MainForm.pUseItemId = 0 Then ' 아이템 사용 중이 아닌 경우
                If Not tempProp.sndResourceName Like String.Empty Then
                    If tempProp.isOpen Then
                        If tempProp.pId = 4 Then
                            PropContainer.GetInstance().GetProp(9).pPb.Visible = False
                        End If
                        tempProp.pb.Image = GetResourceImage(tempProp.resourceName)
                        tempProp.isOpen = False
                    Else
                        If tempProp.pId = 4 Then
                            PropContainer.GetInstance().GetProp(9).pPb.Visible = True
                        End If
                        tempProp.pb.Image = GetResourceImage(tempProp.sndResourceName)
                        tempProp.isOpen = True
                    End If
                End If

                If MainForm.pCurEventId = tempProp.linkEvent.pId Then
                    If tempProp.passRequirement = 0 Then ' 요구 아이템이 없는 프랍의 경우
                        If tempProp.linkItemId <> 0 Then ' 얻게 되는 아이템이 있는 이벤트일 경우
                            If Inventory.GetInstance.IsFull() = False Then
                                If tempProp.linkFormId = 0 Then
                                    Inventory.GetInstance().AddItem(ItemContainer.GetInstance().GetItem(tempProp.linkItemId))
                                    MainForm.pCurEventId = tempProp.linkEvent.pNextId
                                End If
                            Else
                                MsgBox("인벤토리가 가득차서 이벤트를 수행할 수 없습니다.")
                            End If
                        Else ' 얻게 되는 아이템이 없는 이벤트일 경우
                            If tempProp.linkFormId = 0 Then
                                MainForm.pCurEventId = tempProp.linkEvent.pNextId
                            End If
                        End If

                        If tempProp.linkDialogId <> 0 Then ' 대사가 있을 경우
                            PrintDialog(tempProp, True)
                        End If

                        If tempProp.linkFormId <> 0 Then ' 특정 암호, 이벤트 등이 열리는 경우
                            'Temp Code
                            Select Case tempProp.linkFormId
                                Case 10001
                                    DialLockForm.Show()
                                Case 10002
                                    SlidingPuzzleForm.Show()
                                Case 10004
                                    MemoryCardForm.Show()
                            End Select
                        End If
                    Else ' 요구 아이템이 있는 프랍의 경우
                        If tempProp.linkDialogId <> 0 Then
                            PrintDialog(tempProp, False)
                        End If
                    End If
                Else
                    If tempProp.linkDialogId <> 0 Then
                        PrintDialog(tempProp, False)
                    End If
                End If
            Else ' 프랍과의 이벤트 작용이 있는 아이템을 사용하고 있는 경우
                If MainForm.pUseItemId = tempProp.passRequirement Then
                    If MainForm.pCurEventId = tempProp.linkEvent.pId Then
                        Inventory.GetInstance().RemoveItemById(MainForm.pUseItemId)
                        MainForm.pUseItemId = 0
                        MainForm.Cursor = Cursors.Arrow
                        MainForm.pCurEventId = tempProp.linkEvent.pNextId

                        If tempProp.linkDialogId <> 0 Then ' 대사가 있을 경우
                            PrintDialog(tempProp, True)
                        End If

                        If tempProp.linkFormId <> 0 Then ' 연결되는 폼이 있는 경우
                            Select Case tempProp.linkFormId
                                Case 10005
                                    HangmanForm.Show()
                            End Select
                        End If

                        ' <요구아이템>을 사용해 적합한 프랍을 클릭하여 이벤트 진행 가능(Temp)
                        Select Case tempProp.passRequirement
                            Case 101
                                Inventory.GetInstance.AddItem(ItemContainer.GetInstance().GetItem(tempProp.linkHiddenItemId))
                        End Select
                    End If
                End If
            End If
        End If
    End Sub

    Public Sub SubstituteParsingData(_id As Integer)
        id = _id
        Dim data As DataElement = Nothing

        If PropData.GetInstance().FindElementByKey("Id", _id.ToString(), data) Then
            name = data.DataIndexer("Name").value
            resourceName = data.DataIndexer("ResourceName").value
            sndResourceName = data.DataIndexer("SecondResourceName").value
            isOpen = False
            linkEvent.pId = CInt(data.DataIndexer("EventId").value)
            linkEvent.pNextId = CInt(data.DataIndexer("NextEventId").value)
            linkItemId = CInt(data.DataIndexer("Item").value)
            linkHiddenItemId = CInt(data.DataIndexer("HiddenItem").value)
            linkDialogId = CInt(data.DataIndexer("Dialog").value)
            linkFormId = CInt(data.DataIndexer("EventKind").value)
            passRequirement = CInt(data.DataIndexer("PassRequirement").value)
            pb.Width = CInt(data.DataIndexer("Width").value)
            pb.Height = CInt(data.DataIndexer("Height").value)
            pb.SizeMode = PictureBoxSizeMode.StretchImage
        End If
    End Sub

    Public Sub PrintDialog(ByRef subjectProp As Prop, isClear As Boolean)
        If isClear Then
            dialogMgrInst.pTextEnumerator = dialogMgrInst.GetClearDialog(subjectProp.linkDialogId).GetEnumerator()
            dialogMgrInst.ClearDialogBox()
            MainForm.DialogTimer.Enabled = True
        Else
            dialogMgrInst.pTextEnumerator = dialogMgrInst.GetNormalDialog(subjectProp.linkDialogId).GetEnumerator()
            dialogMgrInst.ClearDialogBox()
            MainForm.DialogTimer.Enabled = True
        End If
    End Sub
End Class
