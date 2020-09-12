<%--
  Created by IntelliJ IDEA.
  User: user
  Date: 2019-10-02
  Time: 오후 3:24
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<% request.setCharacterEncoding("UTF-8"); %>

<html>
<head>
    <title>ch06 : request_result.jsp</title></head>
    <style type="text/css">
        div {
            margin-left: auto;
            margin-right: auto;
        }
        #test1 table {
            margin-left: auto;
            margin-right: auto;
            border: 1px solid black;
            border-spacing: 1px;
        }
        tr {
            padding: 5px;
        }
    </style>
<body>
<div>
    <h2>회원 정보</h2>
    <hr>
    <table id="test1"> <!-- 표 생성 -->
        <tr>
            <td>이름</td>
            <td><%=request.getParameter("username")%> </td> <!-- 'username'을 name으로 갖는 파라미터값 요청해서 가져옴. -->
        <tr>
            <td>직업</td>
            <td><%=request.getParameter("job")%></td> <!-- 'job'을 name으로 갖는 파라미터값 요청해서 가져옴 -->
        <tr>
            <td>관심분야</td>
            <td>
<%
	// getParameterValues 메서드를 이용해 "favorite" 로 설정된 form 의 체크박스 값들을 모두 읽어옴.
	String[] favorites = request.getParameterValues("favorite");
/*
	// 배열의 크기만큼 루프롤 돌면서 값을 출력함.
	for(int i=0; i<favorites.length;i++) {
		out.println(favorites[i]+"<BR>");
	}
*/
	// java 5.0 코드
	for(String favorite: favorites) {
		out.println(favorite+"<br>");
	}
%>
    </table>
    <HR>
    <H2>네트워크 정보</H2>
    <table id="test2">
        <tr>
            <td>
            1. 클라이언트 IP 주소 : <%= request.getRemoteAddr() %><br> <!-- 클라이언트의 IP 주소를 요청해서 가져와서 출력 -->
            2. 요청 메서드 : <%= request.getMethod() %><br> <!-- 요청한 메소드를 가져와서 출력 -->
            <%
                Cookie[] cookie = request.getCookies(); // 쿠키를 가져옴
            %>
            3. <%= cookie[0].getName() %> 에 설정된 쿠키값 : <%=cookie[0].getValue() %><br> <!-- 쿠키를 출력 -->
            4. 프로토콜 : <%= request.getProtocol() %> <!-- 프로토콜을 가져와서 출력 -->
            </td>
        </tr>
    </table>
</div>
</body>
</html>
