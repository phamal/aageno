delete from my_links_bids where auctionid > 1000000000 or auctionid < 0;
delete from my_links_plus_bids where webbid_id in (select webbid_id from dpx_webextract_bid where bidid in (select bidid from dpx_webextract where oid > 1000000000));
delete from my_links_plus_bids where webbid_id in (select webbid_id from dpx_webextract_bid where bidid in (select bidid from dpx_webextract where oid in (67815,67874,67875,67877,67878,67897,-10000,-101,-102,-103)));

delete from p2p_order_item where p2p_order_id > 1000000000;
delete from cri_line_item where cri_request_id > 1000000000;
delete from p2p_order where p2p_order_id > 1000000000;
delete from cri_request where agencyoid > 1000000000;
delete from cri_budget_line_budgetcode where budget_line_id in (select budget_line_id from cri_budget_line where agency_oid > 1000000000);
delete from cri_budget_line where agency_oid > 1000000000;
delete from cri_budgetcode where agency_oid > 1000000000;
delete from cri_budgetcode_type where agency_oid > 1000000000;

delete from org_portal_notification where OID > 1000000000;
delete from portal_notification where oid > 1000000000;

commit;

select * from user_constraints where constraint_name = 'BUDGETCODE_ID_FK';
select * from user_constraints where table_name = 'CRI_BUDGET_LINE_BUDGETCODE';
select * from CRI_BUDGET_LINE_BUDGETCODE;
select * from cri_budget_line;

--drop index budgetcode_id_fk;

--alter table cri_budget_line_budgetcode drop constraint 'BUDGETCODE_ID_FK';

commit;


