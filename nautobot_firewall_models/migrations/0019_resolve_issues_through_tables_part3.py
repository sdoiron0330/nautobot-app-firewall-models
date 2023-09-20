# Generated by Django 3.2.21 on 2023-09-18 20:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("ipam", "0038_vlan_group_name_unique_remove_slug"),
        ("nautobot_firewall_models", "0018_resolve_issues_through_tables_part2"),
    ]

    operations = [
        # models.address.addressobjectgroup
        migrations.RemoveField(
            model_name="addressobjectgroup",
            name="address_objects",
        ),
        migrations.DeleteModel(
            name="AddressObjectGroupM2M",
        ),
        migrations.RenameField(
            model_name="addressobjectgroup",
            old_name="new_address_objects",
            new_name="address_objects",
        ),
        migrations.AlterField(
            model_name="addressobjectgroup",
            name="address_objects",
            field=models.ManyToManyField(
                blank=True, related_name="address_object_groups", to="nautobot_firewall_models.AddressObject"
            ),
        ),
        # models.address.fqdn
        migrations.RemoveField(
            model_name="fqdn",
            name="ip_addresses",
        ),
        migrations.DeleteModel(
            name="FQDNIPAddressM2M",
        ),
        migrations.RenameField(
            model_name="fqdn",
            old_name="new_ip_addresses",
            new_name="ip_addresses",
        ),
        migrations.AlterField(
            model_name="fqdn",
            name="ip_addresses",
            field=models.ManyToManyField(blank=True, related_name="fqdns", to="ipam.IPAddress"),
        ),
        # models.user.userobjectgroup
        migrations.RemoveField(
            model_name="userobjectgroup",
            name="user_objects",
        ),
        migrations.DeleteModel(
            name="UserObjectGroupM2M",
        ),
        migrations.RenameField(
            model_name="userobjectgroup",
            old_name="new_user_objects",
            new_name="user_objects",
        ),
        migrations.AlterField(
            model_name="userobjectgroup",
            name="user_objects",
            field=models.ManyToManyField(
                blank=True, related_name="user_object_groups", to="nautobot_firewall_models.UserObject"
            ),
        ),
        # models.zone.zone
        migrations.RemoveField(
            model_name="zone",
            name="interfaces",
        ),
        migrations.RemoveField(
            model_name="zone",
            name="vrfs",
        ),
        migrations.DeleteModel(
            name="ZoneInterfaceM2M",
        ),
        migrations.DeleteModel(
            name="ZoneVRFM2M",
        ),
        migrations.RenameField(
            model_name="zone",
            old_name="new_interfaces",
            new_name="interfaces",
        ),
        migrations.RenameField(
            model_name="zone",
            old_name="new_vrfs",
            new_name="vrfs",
        ),
        migrations.AlterField(
            model_name="zone",
            name="interfaces",
            field=models.ManyToManyField(blank=True, related_name="zones", to="dcim.Interface"),
        ),
        migrations.AlterField(
            model_name="zone",
            name="vrfs",
            field=models.ManyToManyField(blank=True, related_name="zones", to="ipam.VRF"),
        ),
        # models.service.serviceobjectgroup
        migrations.RemoveField(
            model_name="serviceobjectgroup",
            name="service_objects",
        ),
        migrations.DeleteModel(
            name="ServiceObjectGroupM2M",
        ),
        migrations.RenameField(
            model_name="serviceobjectgroup",
            old_name="new_service_objects",
            new_name="service_objects",
        ),
        migrations.AlterField(
            model_name="serviceobjectgroup",
            name="service_objects",
            field=models.ManyToManyField(
                blank=True, related_name="service_object_groups", to="nautobot_firewall_models.ServiceObject"
            ),
        ),
        # models.service.applicationobjectgroup
        migrations.RemoveField(
            model_name="applicationobjectgroup",
            name="application_objects",
        ),
        migrations.DeleteModel(
            name="ApplicationObjectGroupM2M",
        ),
        migrations.RenameField(
            model_name="applicationobjectgroup",
            old_name="new_application_objects",
            new_name="application_objects",
        ),
        migrations.AlterField(
            model_name="applicationobjectgroup",
            name="application_objects",
            field=models.ManyToManyField(
                blank=True, related_name="application_object_groups", to="nautobot_firewall_models.ApplicationObject"
            ),
        ),
        # models.security_policy.policyrule source
        migrations.RemoveField(
            model_name="policyrule",
            name="source_users",
        ),
        migrations.RemoveField(
            model_name="policyrule",
            name="source_user_groups",
        ),
        migrations.RemoveField(
            model_name="policyrule",
            name="source_addresses",
        ),
        migrations.RemoveField(
            model_name="policyrule",
            name="source_address_groups",
        ),
        migrations.RemoveField(
            model_name="policyrule",
            name="source_services",
        ),
        migrations.RemoveField(
            model_name="policyrule",
            name="source_service_groups",
        ),
        migrations.DeleteModel(
            name="SrcAddrM2M",
        ),
        migrations.DeleteModel(
            name="SrcAddrGroupM2M",
        ),
        migrations.DeleteModel(
            name="SrcUserM2M",
        ),
        migrations.DeleteModel(
            name="SrcUserGroupM2M",
        ),
        migrations.DeleteModel(
            name="SrcSvcM2M",
        ),
        migrations.DeleteModel(
            name="SrcSvcGroupM2M",
        ),
        migrations.RenameField(
            model_name="policyrule",
            old_name="new_source_users",
            new_name="source_users",
        ),
        migrations.RenameField(
            model_name="policyrule",
            old_name="new_source_user_groups",
            new_name="source_user_groups",
        ),
        migrations.RenameField(
            model_name="policyrule",
            old_name="new_source_addresses",
            new_name="source_addresses",
        ),
        migrations.RenameField(
            model_name="policyrule",
            old_name="new_source_address_groups",
            new_name="source_address_groups",
        ),
        migrations.RenameField(
            model_name="policyrule",
            old_name="new_source_services",
            new_name="source_services",
        ),
        migrations.RenameField(
            model_name="policyrule",
            old_name="new_source_service_groups",
            new_name="source_service_groups",
        ),
        migrations.AlterField(
            model_name="policyrule",
            name="source_address_groups",
            field=models.ManyToManyField(
                blank=True, related_name="source_policy_rules", to="nautobot_firewall_models.AddressObjectGroup"
            ),
        ),
        migrations.AlterField(
            model_name="policyrule",
            name="source_addresses",
            field=models.ManyToManyField(
                blank=True, related_name="source_policy_rules", to="nautobot_firewall_models.AddressObject"
            ),
        ),
        migrations.AlterField(
            model_name="policyrule",
            name="source_service_groups",
            field=models.ManyToManyField(
                blank=True, related_name="source_policy_rules", to="nautobot_firewall_models.ServiceObjectGroup"
            ),
        ),
        migrations.AlterField(
            model_name="policyrule",
            name="source_services",
            field=models.ManyToManyField(
                blank=True, related_name="source_policy_rules", to="nautobot_firewall_models.ServiceObject"
            ),
        ),
        migrations.AlterField(
            model_name="policyrule",
            name="source_user_groups",
            field=models.ManyToManyField(
                blank=True, related_name="policy_rules", to="nautobot_firewall_models.UserObjectGroup"
            ),
        ),
        migrations.AlterField(
            model_name="policyrule",
            name="source_users",
            field=models.ManyToManyField(
                blank=True, related_name="policy_rules", to="nautobot_firewall_models.UserObject"
            ),
        ),
        # models.security_policy.policyrule destination
        migrations.RemoveField(
            model_name="policyrule",
            name="destination_addresses",
        ),
        migrations.RemoveField(
            model_name="policyrule",
            name="destination_address_groups",
        ),
        migrations.RemoveField(
            model_name="policyrule",
            name="destination_services",
        ),
        migrations.RemoveField(
            model_name="policyrule",
            name="destination_service_groups",
        ),
        migrations.RemoveField(
            model_name="policyrule",
            name="applications",
        ),
        migrations.RemoveField(
            model_name="policyrule",
            name="application_groups",
        ),
        migrations.DeleteModel(
            name="ApplicationM2M",
        ),
        migrations.DeleteModel(
            name="ApplicationGroupM2M",
        ),
        migrations.DeleteModel(
            name="DestAddrGroupM2M",
        ),
        migrations.DeleteModel(
            name="DestAddrM2M",
        ),
        migrations.DeleteModel(
            name="DestSvcM2M",
        ),
        migrations.DeleteModel(
            name="DestSvcGroupM2M",
        ),
        migrations.RenameField(
            model_name="policyrule",
            old_name="new_destination_addresses",
            new_name="destination_addresses",
        ),
        migrations.RenameField(
            model_name="policyrule",
            old_name="new_destination_address_groups",
            new_name="destination_address_groups",
        ),
        migrations.RenameField(
            model_name="policyrule",
            old_name="new_destination_services",
            new_name="destination_services",
        ),
        migrations.RenameField(
            model_name="policyrule",
            old_name="new_destination_service_groups",
            new_name="destination_service_groups",
        ),
        migrations.RenameField(
            model_name="policyrule",
            old_name="new_applications",
            new_name="applications",
        ),
        migrations.RenameField(
            model_name="policyrule",
            old_name="new_application_groups",
            new_name="application_groups",
        ),
        migrations.AlterField(
            model_name="policyrule",
            name="application_groups",
            field=models.ManyToManyField(
                blank=True, related_name="policy_rules", to="nautobot_firewall_models.ApplicationObjectGroup"
            ),
        ),
        migrations.AlterField(
            model_name="policyrule",
            name="applications",
            field=models.ManyToManyField(
                blank=True, related_name="policy_rules", to="nautobot_firewall_models.ApplicationObject"
            ),
        ),
        migrations.AlterField(
            model_name="policyrule",
            name="destination_address_groups",
            field=models.ManyToManyField(
                blank=True, related_name="destination_policy_rules", to="nautobot_firewall_models.AddressObjectGroup"
            ),
        ),
        migrations.AlterField(
            model_name="policyrule",
            name="destination_addresses",
            field=models.ManyToManyField(
                blank=True, related_name="destination_policy_rules", to="nautobot_firewall_models.AddressObject"
            ),
        ),
        migrations.AlterField(
            model_name="policyrule",
            name="destination_service_groups",
            field=models.ManyToManyField(
                blank=True, related_name="destination_policy_rules", to="nautobot_firewall_models.ServiceObjectGroup"
            ),
        ),
        migrations.AlterField(
            model_name="policyrule",
            name="destination_services",
            field=models.ManyToManyField(
                blank=True, related_name="destination_policy_rules", to="nautobot_firewall_models.ServiceObject"
            ),
        ),
        # models.security_policy.policy
        migrations.RemoveField(
            model_name="policy",
            name="policy_rules",
        ),
        migrations.DeleteModel(
            name="PolicyRuleM2M",
        ),
        migrations.RenameField(
            model_name="policy",
            old_name="new_policy_rules",
            new_name="policy_rules",
        ),
        migrations.AlterField(
            model_name="policy",
            name="policy_rules",
            field=models.ManyToManyField(blank=True, related_name="policies", to="nautobot_firewall_models.PolicyRule"),
        ),
    ]
