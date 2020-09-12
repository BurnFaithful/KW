<Global.Microsoft.VisualBasic.CompilerServices.DesignerGenerated()> _
Partial Class MoleCatchingForm2
    Inherits System.Windows.Forms.Form

    'Form은 Dispose를 재정의하여 구성 요소 목록을 정리합니다.
    <System.Diagnostics.DebuggerNonUserCode()> _
    Protected Overrides Sub Dispose(ByVal disposing As Boolean)
        Try
            If disposing AndAlso components IsNot Nothing Then
                components.Dispose()
            End If
        Finally
            MyBase.Dispose(disposing)
        End Try
    End Sub

    'Windows Form 디자이너에 필요합니다.
    Private components As System.ComponentModel.IContainer

    '참고: 다음 프로시저는 Windows Form 디자이너에 필요합니다.
    '수정하려면 Windows Form 디자이너를 사용하십시오.  
    '코드 편집기에서는 수정하지 마세요.
    <System.Diagnostics.DebuggerStepThrough()> _
    Private Sub InitializeComponent()
        Me.components = New System.ComponentModel.Container()
        Me.catchCountLabel = New System.Windows.Forms.Label()
        Me.catchCountNumLabel = New System.Windows.Forms.Label()
        Me.GenTimer = New System.Windows.Forms.Timer(Me.components)
        Me.ShowTimer1 = New System.Windows.Forms.Timer(Me.components)
        Me.ShowTimer2 = New System.Windows.Forms.Timer(Me.components)
        Me.ShowTimer3 = New System.Windows.Forms.Timer(Me.components)
        Me.GameTimer = New System.Windows.Forms.Timer(Me.components)
        Me.timeLabel = New System.Windows.Forms.Label()
        Me.timeShowLabel = New System.Windows.Forms.Label()
        Me.guideLabel = New System.Windows.Forms.Label()
        Me.SuspendLayout()
        '
        'catchCountLabel
        '
        Me.catchCountLabel.AutoSize = True
        Me.catchCountLabel.BackColor = System.Drawing.Color.Transparent
        Me.catchCountLabel.Font = New System.Drawing.Font("굴림", 16.2!, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, CType(129, Byte))
        Me.catchCountLabel.ForeColor = System.Drawing.Color.White
        Me.catchCountLabel.Location = New System.Drawing.Point(12, 41)
        Me.catchCountLabel.Name = "catchCountLabel"
        Me.catchCountLabel.Size = New System.Drawing.Size(236, 28)
        Me.catchCountLabel.TabIndex = 0
        Me.catchCountLabel.Text = "잡은 두더지 수 : "
        '
        'catchCountNumLabel
        '
        Me.catchCountNumLabel.AutoSize = True
        Me.catchCountNumLabel.BackColor = System.Drawing.Color.Transparent
        Me.catchCountNumLabel.Font = New System.Drawing.Font("굴림", 16.2!, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, CType(129, Byte))
        Me.catchCountNumLabel.ForeColor = System.Drawing.Color.White
        Me.catchCountNumLabel.Location = New System.Drawing.Point(251, 41)
        Me.catchCountNumLabel.Name = "catchCountNumLabel"
        Me.catchCountNumLabel.Size = New System.Drawing.Size(29, 28)
        Me.catchCountNumLabel.TabIndex = 1
        Me.catchCountNumLabel.Text = "0"
        '
        'GenTimer
        '
        Me.GenTimer.Enabled = True
        Me.GenTimer.Interval = 1000
        '
        'ShowTimer1
        '
        Me.ShowTimer1.Interval = 800
        '
        'GameTimer
        '
        Me.GameTimer.Enabled = True
        Me.GameTimer.Interval = 1000
        '
        'timeLabel
        '
        Me.timeLabel.AutoSize = True
        Me.timeLabel.BackColor = System.Drawing.Color.Transparent
        Me.timeLabel.Font = New System.Drawing.Font("굴림", 16.2!, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, CType(129, Byte))
        Me.timeLabel.ForeColor = System.Drawing.Color.White
        Me.timeLabel.Location = New System.Drawing.Point(641, 41)
        Me.timeLabel.Name = "timeLabel"
        Me.timeLabel.Size = New System.Drawing.Size(168, 28)
        Me.timeLabel.TabIndex = 2
        Me.timeLabel.Text = "지난 시간 : "
        '
        'timeShowLabel
        '
        Me.timeShowLabel.AutoSize = True
        Me.timeShowLabel.BackColor = System.Drawing.Color.Transparent
        Me.timeShowLabel.Font = New System.Drawing.Font("굴림", 16.2!, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, CType(129, Byte))
        Me.timeShowLabel.ForeColor = System.Drawing.Color.White
        Me.timeShowLabel.Location = New System.Drawing.Point(853, 41)
        Me.timeShowLabel.Name = "timeShowLabel"
        Me.timeShowLabel.Size = New System.Drawing.Size(0, 28)
        Me.timeShowLabel.TabIndex = 3
        '
        'guideLabel
        '
        Me.guideLabel.AutoSize = True
        Me.guideLabel.Location = New System.Drawing.Point(23, 11)
        Me.guideLabel.Name = "guideLabel"
        Me.guideLabel.Size = New System.Drawing.Size(0, 15)
        Me.guideLabel.TabIndex = 4
        '
        'MoleCatchingForm2
        '
        Me.AutoScaleDimensions = New System.Drawing.SizeF(8.0!, 15.0!)
        Me.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font
        Me.BackgroundImage = Global.TeamProject_Team3_EscapeRoom.My.Resources.Resources.bg_moleCatching
        Me.BackgroundImageLayout = System.Windows.Forms.ImageLayout.Stretch
        Me.ClientSize = New System.Drawing.Size(1010, 780)
        Me.Controls.Add(Me.guideLabel)
        Me.Controls.Add(Me.timeShowLabel)
        Me.Controls.Add(Me.timeLabel)
        Me.Controls.Add(Me.catchCountNumLabel)
        Me.Controls.Add(Me.catchCountLabel)
        Me.Margin = New System.Windows.Forms.Padding(3, 4, 3, 4)
        Me.Name = "MoleCatchingForm2"
        Me.Text = "두더지 잡기"
        Me.ResumeLayout(False)
        Me.PerformLayout()

    End Sub

    Friend WithEvents catchCountLabel As Label
    Friend WithEvents catchCountNumLabel As Label
    Friend WithEvents GenTimer As Timer
    Friend WithEvents ShowTimer1 As Timer
    Friend WithEvents ShowTimer2 As Timer
    Friend WithEvents ShowTimer3 As Timer
    Friend WithEvents GameTimer As Timer
    Friend WithEvents timeLabel As Label
    Friend WithEvents timeShowLabel As Label
    Friend WithEvents guideLabel As Label
End Class
