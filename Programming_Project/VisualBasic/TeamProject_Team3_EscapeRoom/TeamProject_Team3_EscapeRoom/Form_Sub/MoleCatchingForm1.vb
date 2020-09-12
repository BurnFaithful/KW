Public Class MoleCatchingForm1

    Private Sub Button1_Click(sender As Object, e As EventArgs) Handles Button1.Click
        Me.Close()
    End Sub

    Private Sub Button2_Click(sender As Object, e As EventArgs) Handles Button2.Click
        MoleCatchingForm2.Show()
    End Sub

    Private Sub MoleCatchingForm1_Load(sender As Object, e As EventArgs) Handles MyBase.Load

    End Sub
End Class