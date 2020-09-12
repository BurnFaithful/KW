<%--
  Created by IntelliJ IDEA.
  User: user
  Date: 2019-10-30
  Time: 오후 2:41
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<% request.setCharacterEncoding("UTF-8"); %>
<jsp:useBean id="address" class="youngmin.address.AddressBean"/>
<jsp:setProperty name="address" property="*"/>
<jsp:useBean id="addressList" class="youngmin.address.AddressManager" scope="application"/>

<%
    addressList.Add(address);
%>

<html>
<head>
    <meta charset="utf-8">
    <title>주소 추가</title>
</head>
<body>
    <h2>등록 내용</h2>
    <hr>

    <p>이름 : <%= address.getUserName() %>
    <p>전화번호 : <%= address.getTel() %>
    <p>이메일 : <%= address.getEmail() %>
    <p>성별 : <%= address.getSex() %>
    <a href="address_list.jsp">목록 보기</a>
</body>
</html>
