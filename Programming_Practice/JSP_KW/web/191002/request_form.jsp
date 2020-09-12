<%--
  Created by IntelliJ IDEA.
  User: user
  Date: 2019-10-02
  Time: 오후 3:24
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>ch06 : request_form.html</title>
    <style type="text/css">
        div {
            text-align: center;
            margin-left: auto;
            margin-right: auto;
        }
        table {
            margin-left: auto;
            margin-right: auto;
            border: 1px solid black;
            border-spacing: 1px;
        }
        tr {
            padding: 5px;
        }
        #btn_row td {
            text-align: center;
        }
    </style>
    <script type="text/javascript">
        document.cookie = "test=OK."; // 쿠키 저장. 이름은 test, 값은 OK.
    </script>

</head>
<body>
<div>
    <h2>회원 정보 입력</h2>
    <hr>
    <form name=form1 method=post action=request_result.jsp> <!-- form 이름은 form1, 전송방식 post, 다음 실행할 페이지 request_result.jsp -->
        <table> <!-- 표 생성 -->
            <tr>
                <td>이름</td>
                <td><input type=text size=10 name=username/></td> <!-- 이름 입력 텍스트박스 -->
            <tr>
                <td>직업</td>
                <td>
                    <select name=job/> <!-- 직업 선택 드롭다운 메뉴 -->
                        <option selected>무직</option>
                        <option>회사원</option>
                        <option>전문직</option>
                        <option>학생</option>
                    </select>
                </td>
            <tr>
                <td>관심분야</td> <!-- 관심분야들은 중복 체크될 수 있게 체크박스 메뉴 -->
                <td>
                    <input type=checkbox name=favorite value="정치"/>정치
                    <input type=checkbox name=favorite value="사회"/>사회
                    <input type=checkbox name=favorite value="정보통신"/>정보통신
                </td>
            <!-- 마지막 열 2개는 병합 -->
            <tr>
                <td id="btn_row" colspan=2>
                    <input type=submit value="확인">
                    <input type=reset value="취소">
                </td>
            </tr>
        </table>
    </form>
</div>
</body>
</html>
