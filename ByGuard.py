
import base64, codecs
magic = 'aW1wb3J0IHJlDQpmcm9tIHVybGxpYi5wYXJzZSBpbXBvcnQgdXJscGFyc2UNCg0KaW1wb3J0IG9zLHN5cw0KdHJ5Og0KICAgIGltcG9ydCBodHRweA0KZXhjZXB0Og0KICAgIGlmIHN5cy5wbGF0Zm9ybS5zdGFydHN3aXRoKCJsaW51eCIpOg0KICAgICAgICBvcy5zeXN0ZW0oInBpcDMgaW5zdGFsbCBodHRweFtodHRwMl0iKQ0KICAgIGVsaWYgc3lzLnBsYXRmb3JtLnN0YXJ0c3dpdGgoImZyZWVic2QiKToNCiAgICAgICAgb3Muc3lzdGVtKCJwaXAzIGluc3RhbGwgaHR0cHhbaHR0cDJdIikNCiAgICBlbHNlOg0KICAgICAgICBvcy5zeXN0ZW0oInBpcCBpbnN0YWxsIGh0dHB4W2h0dHAyXSIpDQoNCg0KaW1wb3J0IGh0dHB4DQpvcy5zeXN0ZW0oJ2Nsc3x8Y2xlYXInKQ0KDQpsb2dvID0gIiIiDQogICAg4pWU4pWQ4pWQ4pWXICAgICAg4pWU4pWQ4pWQ4pWQ4pWXICAgICAgICAgICAgICDilZTilZcNCiAgICDilZHilZTilZfilZEgICAgICDilZHilZTilZDilZfilZEgICAgICAgICAgICAgIOKVkeKVkQ0KICAgIOKVkeKVmuKVneKVmuKVl+KVlOKVlyDilZTilZfilZHilZEg4pWa4pWd4pWU'
love = '4cJK4cJH4cJK4cJH4cJD4cJD4cJKVBXIyBXIxBXIy+XIyBXIxBXIarXIxD0XVPNtVBXIxrXIyBXIxBXIy+XIxrXIxrXIxFQvyMUvyMUvyMUvyMUvyMGvyMQvyMsvyMUvyMUvyMUvyMUvyMbt4cJK4cJEVBXIxrXIyBXIarXIxrXIyBXIy+XIxD0XVPNtVBXIxrXIzhXIxBXIarXIxrXIxrXIzhXIxBXIarXIxrXIxrXIzhXIdrXIxBXIxrXIxrXIzhXIarXIxrXIxrXIzhXIarXIzhXIy+XIxrXIxFQvyMUvyMevyM3vyMRAPvNtVPQvyMevyMQvyMQvyMQvyM3vyMevyMQvyMsvyMGvyM3vyMevyMQvyMQvyMQvyM3vyMevyMQvyMQvyM3vyMevyMQvyMQvyMQvyM3vyMevyM0t4cJn4cJD4cJD4cJqQDbtVPNtVPNtVPQvyMGvyMQvyM3vyMRtVPNtVPNtVPNtVPNtVROwL2qiqFNtVPNAPvNtVPNtVPNtVBXIzhXIxBXIxBXIaFNtVPNtVPNtVPNtVPNtVPNtVPNtVPNAPvVvVt0XQDcwoTSmplORER9GE3IupzD6QDbtVPNtMTIzVS9snJ5cqS9sXUAyoTLcVP0+VR5iozH6QDbtVPNtVPNtVUAyoTLhMJ5xpT9coaEmVQ0trlWwnTIwnlV6VPWbqUEjpmbiY2AbMJAeYzExo3ZgM3IupzDhozI0Y2AbMJAeYzcmVa0APt0X'
god = 'ICAgICAgICBzZWxmLnNlc3Npb24gPSBodHRweC5DbGllbnQoDQogICAgICAgICAgICBodHRwMj1UcnVlLCBoZWFkZXJzPXsidXNlci1hZ2VudCI6ICJERE9TLUdVQVJEIEJ5cGFzc2VyIn0NCiAgICAgICAgKQ0KDQogICAgZGVmIGdldF9jaGVjayhzZWxmKToNCiAgICAgICAgcmV0dXJuIHNlbGYuc2Vzc2lvbi5nZXQoc2VsZi5lbmRwb2ludHNbImNoZWNrIl0pLnRleHQNCg0KICAgIGRlZiBwYXJzZV9jaGVjayhzZWxmLCBjaGVjayk6DQogICAgICAgIHNyYyA9IHJlLmNvbXBpbGUociJuZXcgSW1hZ2VcKFwpLnNyYyA9ICcoLis/KSc7IikNCiAgICAgICAgcmV0dXJuIHNyYy5zZWFyY2goY2hlY2spLmdyb3VwKDEpDQoNCiAgICBkZWYgc3JjX3ZhbGlkYXRvcihzZWxmLCBkb21haW5lLCBzcmMpOg0KICAgICAgICBzZWxmLnNlc3Npb24uZ2V0KGYie2RvbWFpbmV9e3NyY30iKQ0KDQogICAgZGVmIHBhcnNlX2RvbWFpbmUoc2VsZiwgdXJsKToNCiAgICAgICAgdXJsX3BhcnNlID0gdXJscGFyc2UodXJsKQ0KICAgICAgICByZXR1cm4gZiJ7dXJsX3BhcnNlLnNjaGVtZX06Ly97dXJsX3BhcnNl'
destiny = 'Yz5yqTkiL30vQDbAPvNtVPOxMJLtM2I0XUAyoTLfVUIloPjtnTIuMTIlpm1Bo25yXGbAPvNtVPNtVPNtpTSlp2IsMT9gLJyhMFN9VUAyoTLhpTSlp2IsMT9gLJyhMFu1pzjcQDbAPvNtVPNtVPNtL2uyL2ftCFOmMJkzYzqyqS9wnTIwnltcQDbtVPNtVPNtVUOupaAyK2AbMJAeVQ0tp2IfMv5jLKWmMI9wnTIwnluwnTIwnlxAPt0XVPNtVPNtVPOmMJkzYaAlL192LJkcMTS0o3VbpTSlp2IsMT9gLJyhMFjtpTSlp2IsL2uyL2fcQDbtVPNtVPNtVUWyqUIlovOmMJkzYaAyp3Aco24hM2I0XUIloPjtnTIuMTIlpm1bMJSxMKWmXD0XQDcxMT9mM3IupzDtCFORER9GE3IupzDbXD0XpUWcoaDboT9aolxAPaIloPN9VTyhpUI0XPWIHxmiiWbvXD0XLJ5cMTI4VQ0tMTEip2q1LKWxYzqyqPu1pzjcQDccMvOuozyxMKthp3EuqUImK2AiMTHtCG0tZwNjBt0XVPNtVUOlnJ50XPYzwWUzvWwzvWQyvc8hYv4vXD0XVPNtVTyhpUI0XTLv5blW4bPpEJ50MKYvtW3zvMCywoO7qKWfsrrnuBn6xBrttFVcQDbtVPNtpUWcoaDbLJ5cMTI4YaEyrUDcQDcyoUAyBt0XVPNtVUOlnJ50XPYzwWUzvWwycYUbgXHhYv4vXD0X'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))