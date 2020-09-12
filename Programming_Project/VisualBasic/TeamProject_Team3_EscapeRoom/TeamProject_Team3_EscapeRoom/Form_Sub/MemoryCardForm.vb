Public Class MemoryCardForm

    Public Enum eCardKind
        RED
        BLUE
        WHITE
        GREEN
        YELLOW
        ORANGE
        QUANTITY
    End Enum

    Public Structure tagCard
        Dim isSet As Boolean ' 초기 세팅용
        Dim isOpen As Boolean ' 뒤집어져있는지
        Dim isMatch As Boolean ' 맞췄는지
        Dim cardKind As eCardKind
        Dim pb As PictureBox
    End Structure

    Public Const CARD_WIDTH As Integer = 100
    Public Const CARD_HEIGHT As Integer = 150
    Public Const GAP As Integer = 50
    Public Const FALLBACKTIME As Integer = 25

    Private card(eCardKind.QUANTITY * 2 - 1) As tagCard ' 카드 배열변수

    ' 첫번째, 두번째 오픈 카드 체크용 변수
    Private firstCheck As Integer
    Public Property pFirstCheck As Integer
        Get
            Return firstCheck
        End Get
        Set(value As Integer)
            firstCheck = value
        End Set
    End Property
    Private secondCheck As Integer
    Public Property pSecondCheck As Integer
        Get
            Return secondCheck
        End Get
        Set(value As Integer)
            secondCheck = value

            If secondCheck >= 0 And secondCheck <= card.Length Then
                If card(firstCheck).cardKind = card(secondCheck).cardKind Then
                    card(firstCheck).isMatch = True
                    card(secondCheck).isMatch = True
                    firstCheck = -1
                    secondCheck = -1
                Else
                    card(firstCheck).isOpen = False
                    card(secondCheck).isOpen = False
                    ShowTimer.Enabled = True
                End If

                For i = 0 To UBound(card)
                    If Not card(i).isMatch Then
                        completeCheck = False
                        Return
                    End If
                Next
                completeCheck = True
                If completeCheck Then
                    GameTimer.Enabled = False
                    If MsgBox("16 -> 37 -> 58 -> 89 -> 145 -> 42 -> 20 -> ? ->" & vbCrLf &
                              "이 수들은 순환하고 있는 수인 것 같다. 무슨 규칙이 있는건가?",
                              MsgBoxStyle.OkCancel) = MsgBoxResult.Ok Then
                        Dim answer As String = InputBox("답을 입력하세요.")

                        If answer = 4 Then
                            UIClass.GetInstance().pSafePassword(2).Visible = True
                        End If
                    End If
                    UIClass.GetInstance().pQuestionBtn(1).Visible = True
                    MainForm.pCurEventId = 4
                    Me.Close()
                End If
            End If
        End Set
    End Property

    Private firstPB, secondPB As PictureBox
    Private elaspedTime As Integer
    Private completeCheck As Boolean

    Private Sub SubGameForm2_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        SetForm()

        pFirstCheck = -1
        pSecondCheck = -1
        elaspedTime = 0
        completeCheck = False
        SetCard()
    End Sub

    ' Form 관련값 세팅
    Private Sub SetForm()
        Me.Width = WINDOWS_WIDTH - 256
        Me.Height = WINDOWS_HEIGHT

        Dim guideLabel As New Label
        guideLabel.AutoSize = True
        guideLabel.Font = New Font(Form.DefaultFont.FontFamily, 12, FontStyle.Bold)
        guideLabel.Location = New Point(5, 5)
        guideLabel.Text = FALLBACKTIME & " 초 안에 클리어해야 한다."
        Me.Controls.Add(guideLabel)
    End Sub

    Private Sub SetCard()
        ' 기본 변수 세팅
        For i = 0 To UBound(card)
            card(i).isSet = False
            card(i).isOpen = False
            card(i).isMatch = False
        Next

        Dim setCount As eCardKind = 0 ' RED
        Dim firstCard, secondCard As Integer
        firstCard = secondCard = 0

        ' 카드 짝 세팅
        Do Until setCount = eCardKind.QUANTITY
            firstCard = RandomInt(card.Length)
            secondCard = RandomInt(card.Length)

            If firstCard <> secondCard Then
                If Not card(firstCard).isSet And Not card(secondCard).isSet Then
                    card(firstCard).cardKind = setCount
                    card(secondCard).cardKind = setCount
                    card(firstCard).isSet = True
                    card(secondCard).isSet = True
                    setCount += 1
                End If
            End If
        Loop

        For i = 0 To UBound(card)
            SetCardImage(i)
        Next
    End Sub

    Private Sub SetCardImage(index As Integer)
        ' 카드 이미지 관련 속성 세팅
        For i = 0 To UBound(card)
            card(i).pb = New PictureBox()
            card(i).pb.Name = "CardPB" & i
            card(i).pb.Width = CARD_WIDTH
            card(i).pb.Height = CARD_HEIGHT
            card(i).pb.Left = 100 + (i Mod 4) * (CARD_WIDTH + GAP)
            card(i).pb.Top = 100 + (i \ 4) * (CARD_HEIGHT + GAP)
            card(i).pb.BackColor = Color.Black
            Me.Controls.Add(card(i).pb)

            AddHandler card(i).pb.Click, AddressOf OpenCard
        Next
    End Sub

    ' Card Click Event
    Private Sub OpenCard(sender As Object, e As EventArgs)
        If ShowTimer.Enabled = False Then
            Dim cardIndex As Integer = 0
            Dim tempPB As PictureBox = CType(sender, PictureBox)
            For i = 0 To UBound(card)
                If card(i).pb.Name Like tempPB.Name Then
                    cardIndex = i
                    Exit For
                End If
            Next

            If Not card(cardIndex).isOpen Then
                card(cardIndex).isOpen = True
                Select Case card(cardIndex).cardKind
                    Case eCardKind.RED
                        tempPB.BackColor = Color.Red
                    Case eCardKind.BLUE
                        tempPB.BackColor = Color.Blue
                    Case eCardKind.WHITE
                        tempPB.BackColor = Color.White
                    Case eCardKind.GREEN
                        tempPB.BackColor = Color.LightGreen
                    Case eCardKind.YELLOW
                        tempPB.BackColor = Color.Yellow
                    Case eCardKind.ORANGE
                        tempPB.BackColor = Color.Orange
                End Select
                If pFirstCheck < 0 Then
                    pFirstCheck = cardIndex
                    firstPB = tempPB
                Else
                    pSecondCheck = cardIndex
                    secondPB = tempPB
                End If
            End If
        End If
    End Sub

    ' 제한 시간
    Private Sub GameTimer_Tick(sender As Object, e As EventArgs) Handles GameTimer.Tick
        elaspedTime += 1
        Label2.Text = elaspedTime & " 초"

        If elaspedTime >= FALLBACKTIME Then
            GameTimer.Enabled = False
            If completeCheck = False Then
                If MsgBox("제한 시간 안에 해결하지 못했습니다. 다시 시도하세요.") = MsgBoxResult.Ok Then
                    Me.Close()
                End If
            End If
        End If
    End Sub

    ' 오픈한 두 카드 보여주는 타이머
    Private Sub ShowTimer_Tick(sender As Object, e As EventArgs) Handles ShowTimer.Tick
        pFirstCheck = -1
        pSecondCheck = -1
        firstPB.BackColor = Color.Black
        secondPB.BackColor = Color.Black
        ShowTimer.Enabled = False
    End Sub
End Class