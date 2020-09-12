<%--
  Created by IntelliJ IDEA.
  User: user
  Date: 2019-10-30
  Time: 오후 2:43
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ page import="youngmin.address.*" %>
<jsp:useBean id="addressList" class="youngmin.address.AddressManager" scope="application"/>
<html>
<head>
    <meta charset="utf-8">
    <title>주소록</title>
</head>
<body>
    <div>
        <h2>주소록</h2>
        <hr>

        <a href="address_form.html">주소 추가</a><br>
        <a href="address_clear.jsp">모두 지우기</a>
        <table>
            <thead>
                <th>이름</th> <th>전화번호</th> <th>이메일</th> <th>성별</th>
            </thead>
            <tbody>
        <%
            for(AddressBean row : addressList.getAddress())
            {
        %>
                <tr>
                    <td><%= row.getUserName()%></td>
                    <td><%= row.getTel()%></td>
                    <td><%= row.getEmail()%></td>
                    <td><%= row.getSex()%></td>
                </tr>
        <%
            }
        %>
            </tbody>
        </table>
    </div>
</body>
</html>
