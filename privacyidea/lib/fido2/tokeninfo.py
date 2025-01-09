class Fido2TokenInfo(object):
    """
    Token info fields used by WebAuthn
    """

    PUB_KEY = "pubKey"
    ORIGIN = "origin"
    AAGUID = "aaguid"
    ATTESTATION_LEVEL = "attestation_level"
    ATTESTATION_ISSUER = "attestation_issuer"
    ATTESTATION_SERIAL = "attestation_serial"
    ATTESTATION_SUBJECT = "attestation_subject"
    RELYING_PARTY_ID = "relying_party_id"
    RELYING_PARTY_NAME = "relying_party_name"
