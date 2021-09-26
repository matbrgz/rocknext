frappe.treeview_settings["Compliance Procedure"] = {
	ignore_fields:["parent_compliance_procedure"],
	get_tree_nodes: 'erpnext.compliance.doctype.compliance_procedure.compliance_procedure.get_children',
	add_tree_node: 'erpnext.compliance.doctype.compliance_procedure.compliance_procedure.add_node',
	filters: [
		{
			fieldname: "parent_compliance_procedure",
			fieldtype: "Link",
			options: "Compliance Procedure",
			label: __("Compliance Procedure"),
			get_query: function() {
				return {
					filters: [["Compliance Procedure", 'is_group', '=', 1]]
				};
			}
		},
	],
	breadcrumb: "Compliance Management",
	disable_add_node: true,
	root_label: "All Compliance Procedures",
	get_tree_root: false,
	menu_items: [
		{
			label: __("New Compliance Procedure"),
			action: function() {
				frappe.new_doc("Compliance Procedure", true);
			},
			condition: 'frappe.boot.user.can_create.indexOf("Compliance Procedure") !== -1'
		}
	],
	onload: function(treeview) {
		treeview.make_tree();
	},
};
