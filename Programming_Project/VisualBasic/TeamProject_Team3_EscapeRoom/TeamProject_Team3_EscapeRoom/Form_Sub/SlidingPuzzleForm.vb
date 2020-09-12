Public Class SlidingPuzzleForm

    Public Structure tagPiece
        Dim id As Integer
        Dim orgPos As Point
        Dim btn As Button
        Dim isEmpty As Boolean
    End Structure

    Private piece(2, 2) As tagPiece

    Private Sub SlidingPuzzleForm_Load(sender As Object, e As EventArgs) Handles MyBase.Load
        For i = 0 To UBound(piece, 1)
            For j = 0 To UBound(piece, 2)
                piece(i, j).id = (i * 3 + j)
                piece(i, j).orgPos = New Point(100 + (100 + 20) * j, 25 + (100 + 20) * i)

                piece(i, j).btn = New Button()
                piece(i, j).btn.Text = piece(i, j).id + 1
                piece(i, j).btn.Font = New Font(Form.DefaultFont.FontFamily, 12, FontStyle.Bold)
                piece(i, j).btn.Name = "PieceBtn" & piece(i, j).btn.Text
                piece(i, j).btn.Width = 100
                piece(i, j).btn.Height = 100
                piece(i, j).btn.Location = piece(i, j).orgPos
                Me.Controls.Add(piece(i, j).btn)

                AddHandler piece(i, j).btn.Click, AddressOf Event_PieceClick

                piece(i, j).isEmpty = False
            Next
        Next
        piece(2, 2).isEmpty = True
        piece(2, 2).btn.Visible = Not piece(2, 2).isEmpty

        SetPuzzle(100)
    End Sub

    Public Sub Swap(ByRef pieceBtn1 As Button, ByRef pieceBtn2 As Button)
        pieceBtn1.Visible = False
        pieceBtn2.Visible = True

        Dim temp As String

        temp = pieceBtn1.Text
        pieceBtn1.Text = pieceBtn2.Text
        pieceBtn2.Text = temp
    End Sub

    Public Sub Event_PieceClick(sender As Object, e As EventArgs)
        Dim srcBtn As Button = CType(sender, Button)
        Dim row, col As Integer

        For i = 0 To UBound(piece, 1)
            For j = 0 To UBound(piece, 2)
                If piece(i, j).orgPos = srcBtn.Location Then
                    row = i
                    col = j
                    Exit For
                End If
            Next
        Next

        MovePiece(row, col)
    End Sub

    Public Function MovePiece(_row As Integer, _col As Integer) As Boolean
        If _row - 1 >= 0 Then
            If piece(_row - 1, _col).isEmpty Then
                piece(_row - 1, _col).isEmpty = False
                piece(_row, _col).isEmpty = True
                Swap(piece(_row, _col).btn, piece(_row - 1, _col).btn)
                CheckComplete()
                Return True
            End If
        End If
        If _row + 1 <= UBound(piece, 1) Then
            If piece(_row + 1, _col).isEmpty Then
                piece(_row + 1, _col).isEmpty = False
                piece(_row, _col).isEmpty = True
                Swap(piece(_row, _col).btn, piece(_row + 1, _col).btn)
                CheckComplete()
                Return True
            End If
        End If
        If _col - 1 >= 0 Then
            If piece(_row, _col - 1).isEmpty Then
                piece(_row, _col - 1).isEmpty = False
                piece(_row, _col).isEmpty = True
                Swap(piece(_row, _col).btn, piece(_row, _col - 1).btn)
                CheckComplete()
                Return True
            End If
        End If
        If _col + 1 <= UBound(piece, 2) Then
            If piece(_row, _col + 1).isEmpty Then
                piece(_row, _col + 1).isEmpty = False
                piece(_row, _col).isEmpty = True
                Swap(piece(_row, _col).btn, piece(_row, _col + 1).btn)
                CheckComplete()
                Return True
            End If
        End If

        Return False
    End Function

    Public Sub SetPuzzle(moveCnt As Integer)
        Dim moveNum As Integer = 0
        Dim row, col As Integer

        Do Until moveNum = moveCnt
            row = RandomInt(UBound(piece, 1) + 1)
            col = RandomInt(UBound(piece, 2) + 1)
            If MovePiece(row, col) Then
                moveNum += 1
            End If
        Loop
    End Sub

    Public Function CheckComplete() As Boolean
        For i = 0 To UBound(piece, 1)
            For j = 0 To UBound(piece, 2)
                If piece(i, j).btn.Text <> piece(i, j).id + 1 Then
                    Return False
                End If
            Next
        Next

        If MsgBox("818-821-683-248-540-???. 물음표의 1의 자리.",
                          MsgBoxStyle.OkCancel) = MsgBoxResult.Ok Then

            Dim answer As String = InputBox("답을 입력하세요.")

            If answer = 4 Then
                UIClass.GetInstance().pSafePassword(3).Visible = True
            End If
        End If

        UIClass.GetInstance().pQuestionBtn(2).Visible = True
        MainForm.pCurEventId = 6
        Me.Close()
        Return True
    End Function

    Public Sub Cheat()
        For i = 0 To UBound(piece, 1)
            For j = 0 To UBound(piece, 2)
                piece(i, j).btn.Text = piece(i, j).id + 1
            Next
        Next

        CheckComplete()
    End Sub

    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
        Cheat()
    End Sub
End Class