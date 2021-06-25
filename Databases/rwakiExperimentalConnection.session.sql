SELECT *
FROM customer_table;

--Joining multiple tables

SELECT T1.user, T2.tid, T2.name, T3.type, T1.mid
FROM T1
RIGHT JOIN T2 ON T1.mid = T2.mid
LEFT JOIN T3 ON T2.tid = T3.tid;

--for multiple join columns 
ON a.userid = b.sourceid AND a.listid = b.destinationid;

-- staging to trt
-- then resultant table to reball


SELECT T1.user, T2.tid, T2.name, T3.type, T1.mid
FROM T1
RIGHT JOIN T2 ON T1.mid = T2.mid
LEFT JOIN T3 ON T2.tid = T3.tid;


--using an SQL alias in a multi join and with conditions


--E.g 1
SELECT *
FROM new_product_to_category ptc
LEFT JOIN new_product_to_store pts ON pts.product_id = ptc.product_id 
     AND ptc.store_id = pts.store_id
LEFT JOIN new_product_description pd ON pts.product_id = pd.product_id
WHERE ptc.category_id = 1507
  AND pts.store_id = 3;


--E.g 2
--https://stackoverflow.com/questions/14830410/multiple-table-joins-with-where-clause 

  select distinct(a.section_id) as id,
        a.title,
        a.description,
        c.status
 from Sections a 
 left join SectionMembers b on a.section_id = b.section_id
 inner join MemberStatus c on b.status_code = c.status_code
 where (a.section_ownerid = 100 and b.memberid = 200)
       or (a.section_ownerid = 100); 

--E.g 3
-- Using aggregate and groupBy
-- https://stackoverflow.com/questions/1242121/sql-join-group-by-on-three-tables-to-get-totals 

SELECT i.invoiceid, 
sum(case when i.amount is not null then i.amount else 0 end), 
sum(case when i.amount is not null then i.amount else 0 end) - sum(case when p.amount is not null then p.amount else 0 end) AS amountdue
FROM invoices i
LEFT JOIN invoicepayments ip ON i.invoiceid = ip.invoiceid
LEFT JOIN payments p ON ip.paymentid = p.paymentid
LEFT JOIN customers c ON p.customerid = c.customerid
WHERE c.customernumber = '100'
GROUP BY i.invoiceid