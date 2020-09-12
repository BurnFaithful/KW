<%--
  Created by IntelliJ IDEA.
  User: user
  Date: 2019-10-02
  Time: 오후 2:29
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
    <meta charset="UTF-8">
    <title>상품 선택 화면</title>
</head>
<body>
    <%
        request.setCharacterEncoding("UTF-8");

        session.setAttribute("username", request.getParameter("username"));
    %>
    <h2>상품 선택</h2>
    <hr>
    <%=session.getAttribute("username") %> 님이 로그인한 상태입니다.
    <hr>
    <form name="form1" method="POST" action="add.jsp">
        <select name="product">
            <option>사과</option>
            <option>귤</option>
            <option>파인애플</option>
            <option>자몽</option>
            <option>레몬</option>
        </select>
        <input type="submit" value="추가">
    </form>
    <a href="checkOut.jsp">계산</a>
</body>
</html>
