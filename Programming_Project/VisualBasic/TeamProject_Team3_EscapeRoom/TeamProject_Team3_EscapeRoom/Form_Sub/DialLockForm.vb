Public Class DialLockForm

    Public Const dialNum As Integer = 7

    Private password As String = "8144698"
    Public ReadOnly Property pPassword As String
        Get
            Return password
        End Get
    End Property
    ' 쪽지 1 8
    ' 쪽지 2 1
    ' TV (메모리카드) 힌트 4
    ' 태블릿 (두더지 잡기) 힌트 4
    ' 도어락 (행맨) 힌트 6
    ' 데스크탑 (숫자 퍼즐) 힌트 9
    ' 금고 (마우스 미로) 힌트 8

    Private lockNum As Integer

    Private dialBtn(dialNum - 1) As Button
    Private openBtn As Button

    Private Sub DialLockForm_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        Label2.Text = password

        For i = 0 To UBound(dialBtn)
            dialBtn(i) = New Button()
            dialBtn(i).Width = 50
            dialBtn(i).Height = 25
            dialBtn(i).Location = New Point((Me.ClientSize.Width - dialBtn(i).Width) / 2, 120 + (dialBtn(i).Height + 10) * i)
            dialBtn(i).Text = 0
            Me.Controls.Add(dialBtn(i))

            AddHandler dialBtn(i).MouseEnter, AddressOf Event_DialBtn_MouseEnter
            AddHandler dialBtn(i).MouseWheel, AddressOf Event_DialBtn_MouseWheel
        Next
        openBtn = New Button()
        openBtn.Width = 100
        openBtn.Height = 50
        openBtn.Location = New Point(dialBtn(0).Location.X - (openBtn.Width / 4), dialBtn(0).Location.Y - openBtn.Height - 10)
        openBtn.Text = "Open"
        Me.Controls.Add(openBtn)
        AddHandler openBtn.MouseClick, AddressOf Event_OpenBtn_Click
    End Sub

    Public Sub Event_DialBtn_MouseEnter(sender As Object, e As EventArgs)
        Dim tempBtn As Button = CType(sender, Button)

        lockNum = tempBtn.Text
    End Sub

    Public Sub Event_DialBtn_MouseWheel(sender As Object, e As MouseEventArgs)
        WheelLock(sender, e)
    End Sub

    Public Function Event_OpenBtn_Click()
        For i = 0 To UBound(dialBtn)
            If dialBtn(i).Text <> password(i) Then
                MsgBox("이 비밀번호가 아닌 것 같다.")
                Return False
            End If
        Next

        If MsgBox("금고를 열어보니 열쇠 하나가 있었다.", MsgBoxStyle.OkOnly) = MsgBoxResult.Ok Then
            Me.Close()
            MainForm.pCurEventId = 9
            Inventory.GetInstance().AddItem(ItemContainer.GetInstance().GetItem(105))
        End If
        Return True
    End Function

    Public Sub WheelLock(sender As Object, e As MouseEventArgs)
        Dim tempBtn As Button = CType(sender, Button)

        If e.Delta >= UP_WHEEL_VALUE Then
            If tempBtn.Text < 9 Then
                lockNum += 1
                tempBtn.Text = lockNum
            End If
        ElseIf e.Delta <= DOWN_WHEEL_VALUE Then
            If tempBtn.Text > 0 Then
                lockNum -= 1
                tempBtn.Text = lockNum
            End If
        End If
    End Sub

    Private Sub ExitBtn_Click(sender As Object, e As EventArgs) Handles ExitBtn.Click
        Me.Close()
    End Sub

    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
        PointerMaze.Show()
    End Sub
End Class