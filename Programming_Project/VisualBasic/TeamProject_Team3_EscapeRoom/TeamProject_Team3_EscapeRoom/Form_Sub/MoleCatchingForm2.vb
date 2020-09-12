Public Class MoleCatchingForm2

    Public Structure tagMole
        Dim pb As PictureBox
        Dim isGen As Boolean
    End Structure

    Public Const CLEAR_LIMIT As Integer = 10
    Public Const GAME_TIME As Integer = 15

    Private moleArray() As tagMole
    Private genMole(3) As tagMole
    Private genInterval As Integer
    Private showInterval As Integer

    Private catchNum As Integer
    Private elapsedTime As Integer
    Private isClear As Boolean

    Private Sub MoleCatching_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        catchNum = 0
        elapsedTime = 0
        isClear = False

        guideLabel.Text = GAME_TIME & " 초 동안 " & CLEAR_LIMIT & " 마리 이상 잡아야 합니다."
        guideLabel.BackColor = Color.Transparent
        guideLabel.Font = New Font(Form.DefaultFont.FontFamily, 16, FontStyle.Bold)
        guideLabel.ForeColor = Color.White

        Dim placementCalcVar As Integer
        If MoleCatchingForm1.ComboBox1.SelectedItem Is Nothing Then
            ReDim moleArray(15)
            placementCalcVar = 4
        Else
            ReDim moleArray(CInt(MoleCatchingForm1.ComboBox1.SelectedItem) - 1)
            placementCalcVar = Math.Sqrt(MoleCatchingForm1.ComboBox1.SelectedItem)
        End If

        Select Case MoleCatchingForm1.ComboBox2.SelectedIndex
            Case 0
                genInterval = 3000
            Case 1
                genInterval = 2000
            Case 2
                genInterval = 1000
            Case Else
                genInterval = 2000
        End Select
        showInterval = genInterval - 100
        GenTimer.Interval = genInterval
        ShowTimer1.Interval = showInterval

        For i = 0 To UBound(moleArray)
            moleArray(i).isGen = False

            moleArray(i).pb = New PictureBox()
            moleArray(i).pb.Width = 100
            moleArray(i).pb.Height = 100
            moleArray(i).pb.Location = New Point(150 + (moleArray(i).pb.Width + 20) * (i Mod placementCalcVar), 100 + (moleArray(i).pb.Height + 20) * (i \ placementCalcVar))
            moleArray(i).pb.BackColor = Color.Transparent
            moleArray(i).pb.SizeMode = PictureBoxSizeMode.StretchImage
            moleArray(i).pb.Image = GetResourceImage("tunnel")
            Me.Controls.Add(moleArray(i).pb)

            AddHandler moleArray(i).pb.MouseDown, AddressOf Event_MoleClick
        Next

        For i = 0 To UBound(genMole)
            genMole(i).pb = New PictureBox()
        Next
    End Sub

    Public Sub Event_MoleClick(sender As Object, e As MouseEventArgs)
        If e.Button = MouseButtons.Left Then
            Dim tempPB As PictureBox = CType(sender, PictureBox)

            For i = 0 To UBound(moleArray)
                If moleArray(i).isGen Then
                    If tempPB Is moleArray(i).pb Then
                        tempPB.Image = GetResourceImage("tunnel")
                        catchNum += 1
                        catchCountNumLabel.Text = catchNum
                        Exit For
                    End If
                End If
            Next
        End If
    End Sub

    Private Sub GenTimer_Tick(sender As Object, e As EventArgs) Handles GenTimer.Tick
        ' 랜덤 확률 조정
        Dim rndGenMole As Integer = RandomInt(11)
        Dim genMoleNum As Integer = 0
        If rndGenMole = 10 Then
            genMoleNum = 3
        ElseIf rndGenMole > 6 And rndGenMole < 10 Then
            genMoleNum = 2
        Else
            genMoleNum = 1
        End If
        ' 랜덤 확률 조정

        ' 2개 이상 나올 때
        If genMoleNum > 1 Then
            ' 값 배열 초기화 (땅굴 개수만큼)
            Dim rndGenIndex(moleArray.Length - 1) As Integer
            For i = 0 To UBound(rndGenIndex)
                rndGenIndex(i) = i
            Next

            ' 값 셔플 (땅굴 개수만큼)
            For i = 0 To 100
                Dim temp As Integer

                Dim src As Integer = RandomInt(moleArray.Length)
                Dim dst As Integer = RandomInt(moleArray.Length)

                temp = rndGenIndex(src)
                rndGenIndex(src) = rndGenIndex(dst)
                rndGenIndex(dst) = temp
            Next

            ' 셔플 값 토대로 두더지 설정
            Dim genMoleIndex(genMoleNum - 1) As Integer
            For i = 0 To UBound(genMoleIndex)
                genMoleIndex(i) = rndGenIndex(i)
                moleArray(genMoleIndex(i)).pb.Image = GetResourceImage("mole")
                moleArray(genMoleIndex(i)).isGen = True
                genMole(i) = moleArray(genMoleIndex(i))
            Next
            ' 1개만 나올 때
        Else
            Dim genMoleIndex As Integer
            genMoleIndex = RandomInt(moleArray.Count)
            moleArray(genMoleIndex).pb.Image = GetResourceImage("mole")
            moleArray(genMoleIndex).isGen = True
            genMole(0) = moleArray(genMoleIndex)
        End If

        ShowTimer1.Enabled = True
    End Sub

    Private Sub ShowTimer_Tick(sender As Object, e As EventArgs) Handles ShowTimer1.Tick
        ShowTimer1.Enabled = False
        For i = 0 To UBound(genMole)
            genMole(i).pb.Image = GetResourceImage("tunnel")
            genMole(i).isGen = False
        Next
    End Sub

    Private Sub GameTimer_Tick(sender As Object, e As EventArgs) Handles GameTimer.Tick
        elapsedTime += 1
        timeShowLabel.Text = elapsedTime & " 초"

        If elapsedTime >= GAME_TIME Then
            GameTimer.Enabled = False
            GenTimer.Enabled = False

            If catchNum >= CLEAR_LIMIT Then
                If MsgBox("6 + 3 = 39" & vbCrLf &
                  "7 + 1 = 68" & vbCrLf &
                  "8 + 6 = 214" & vbCrLf &
                  "9 + 2 = 711" & vbCrLf &
                  "5 + 4 = ??" & vbCrLf &
                  "정답의 1의 자리.", MsgBoxStyle.OkCancel) = MsgBoxResult.Ok Then
                    Dim answer As String = InputBox("답을 입력하세요.")

                    If answer = 9 Then
                        UIClass.GetInstance().pSafePassword(5).Visible = True
                    End If
                End If
                Me.Close()
                Inventory.GetInstance().RemoveItem(ItemContainer.GetInstance().GetItem(106))
                UIClass.GetInstance().pQuestionBtn(4).Visible = True
            Else
                If MsgBox("실패.") = MsgBoxResult.Ok Then
                    Me.Close()
                End If
            End If
        End If
    End Sub
End Class