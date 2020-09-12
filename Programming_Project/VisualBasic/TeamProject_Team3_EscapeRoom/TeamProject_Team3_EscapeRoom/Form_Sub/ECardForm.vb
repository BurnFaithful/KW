Public Class ECardForm

    Public Const CARD_NUM As Integer = 4

    Public Enum eAttribute
        EMPEROR
        CITIZEN
        SLAVE
    End Enum

    Public Enum eResult
        WIN
        DRAW
        LOSE
    End Enum

    Public Structure tagCard
        Dim attribute As eAttribute
        Dim btn As Button
    End Structure

    Private isHeadStart As Boolean
    Private gameTurnCnt As Integer

    Private playerDec(CARD_NUM) As tagCard
    Private comDec(CARD_NUM) As tagCard

    Private playerPoint As New Point
    Private comPoint As New Point
    Private playerOpen As tagCard
    Private comOpen As tagCard

    Private result As eResult

    Private comRnd(CARD_NUM) As Integer ' Temp

    Private Sub SubGameForm1_Load(sender As Object, e As EventArgs) Handles MyBase.Load

        playerPoint = New Point(250, 175)
        comPoint = New Point(450, 175)

        isHeadStart = IIf(RandomInt(11) > 5, True, False)

        SetCard(isHeadStart)
    End Sub

    Public Sub SetCard(headStart As Boolean)
        gameTurnCnt = 0

        For i = 0 To UBound(comRnd)
            comRnd(i) = i
        Next

        For i = 0 To 100
            Dim temp As Integer
            Dim src, dst As Integer

            src = RandomInt(comRnd.Length)
            dst = RandomInt(comRnd.Length)

            temp = comRnd(src)
            comRnd(src) = comRnd(dst)
            comRnd(dst) = temp
        Next

        For i = 0 To CARD_NUM
            playerDec(i).btn = New Button()
            playerDec(i).btn.Width = 100
            playerDec(i).btn.Height = 100
            playerDec(i).btn.Location = New Point(100 + (playerDec(i).btn.Width + 20) * i, 25)

            comDec(i).btn = New Button()
            comDec(i).btn.Width = 100
            comDec(i).btn.Height = 100
            comDec(i).btn.Location = New Point(100 + (comDec(i).btn.Width + 20) * i, 325)

            If i = 0 Then
                If headStart Then
                    playerDec(i).attribute = eAttribute.EMPEROR
                    playerDec(i).btn.Text = "황제"
                    comDec(i).attribute = eAttribute.SLAVE
                    comDec(i).btn.Text = "노예"
                Else
                    playerDec(i).attribute = eAttribute.SLAVE
                    playerDec(i).btn.Text = "노예"
                    comDec(i).attribute = eAttribute.EMPEROR
                    comDec(i).btn.Text = "황제"
                End If
            Else
                playerDec(i).attribute = eAttribute.CITIZEN
                playerDec(i).btn.Text = "시민"
                comDec(i).attribute = eAttribute.CITIZEN
                comDec(i).btn.Text = "시민"
            End If

            AddHandler playerDec(i).btn.Click, AddressOf Event_CardClick

            Me.Controls.Add(playerDec(i).btn)
            Me.Controls.Add(comDec(i).btn)
        Next
    End Sub

    Public Sub Event_CardClick(sender As Object, e As EventArgs)
        Dim tempBtn As Button = CType(sender, Button)

        For i = 0 To UBound(playerDec)
            If playerDec(i).btn Is tempBtn Then
                playerOpen = playerDec(i)
                Exit For
            End If
        Next

        tempBtn.Location = playerPoint

        comDec(comRnd(gameTurnCnt)).btn.Location = comPoint
        comOpen = comDec(comRnd(gameTurnCnt))
        gameTurnCnt += 1

        If playerOpen.attribute = eAttribute.CITIZEN And comOpen.attribute = eAttribute.CITIZEN Then
            result = eResult.DRAW
        ElseIf (playerOpen.attribute = eAttribute.CITIZEN And comOpen.attribute = eAttribute.EMPEROR) OrElse
                (playerOpen.attribute = eAttribute.SLAVE And comOpen.attribute = eAttribute.CITIZEN) OrElse
                (playerOpen.attribute = eAttribute.EMPEROR And comOpen.attribute = eAttribute.SLAVE) Then
            result = eResult.LOSE
        ElseIf (playerOpen.attribute = eAttribute.CITIZEN And comOpen.attribute = eAttribute.SLAVE) OrElse
                (playerOpen.attribute = eAttribute.SLAVE And comOpen.attribute = eAttribute.EMPEROR) OrElse
                (playerOpen.attribute = eAttribute.EMPEROR And comOpen.attribute = eAttribute.CITIZEN) Then
            result = eResult.WIN
        End If

        Select Case result
            Case eResult.DRAW
                Label2.Text = "비김"
            Case eResult.LOSE
                Label2.Text = "짐"
            Case eResult.WIN
                Label2.Text = "이김"
        End Select

        For i = 0 To UBound(playerDec)
            If playerDec(i).btn IsNot Nothing Then
                If playerDec(i).btn IsNot playerOpen.btn Then
                    playerDec(i).btn.Enabled = False
                End If
            End If
        Next

        ShowTimer.Enabled = True
    End Sub

    Private Sub ShowTimer_Tick(sender As Object, e As EventArgs) Handles ShowTimer.Tick
        Me.Controls.Remove(playerOpen.btn)
        Me.Controls.Remove(comOpen.btn)

        For i = 0 To UBound(playerDec)
            If playerDec(i).btn IsNot Nothing Then
                playerDec(i).btn.Enabled = True
            End If
        Next

        If result = eResult.LOSE OrElse result = eResult.WIN Then
            For i = 0 To UBound(playerDec)
                If playerDec(i).btn IsNot Nothing Then
                    Me.Controls.Remove(playerDec(i).btn)
                End If
            Next
            For i = 0 To UBound(comDec)
                If comDec(i).btn IsNot Nothing Then
                    Me.Controls.Remove(comDec(i).btn)
                End If
            Next
            isHeadStart = Not isHeadStart
            SetCard(isHeadStart)
        End If

        ShowTimer.Enabled = False
        Label2.Text = String.Empty
    End Sub
End Class