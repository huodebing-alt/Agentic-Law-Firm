# Compliance and Disclaimer Notes

See the project-root `DISCLAIMER.md` for the binding statement. This
document collects related compliance notes for the operator.

## Use of third-party data sources

Several MCP connectors (PKULaw, WKInfo, ChinaLawInfo, Westlaw,
LexisNexis, TianYanCha, QiChaCha, FaDaDa, e签宝, iManage,
NetDocuments) are proprietary or paid services. Each connector's
`README.md` notes the access requirement. The operator is
responsible for complying with each provider's terms of service.

Scraping the public-but-restricted 裁判文书网 may breach the site's
terms after the 2024 access changes; the stub does not scrape. For
production use, consider a paid aggregator or a locally cached
snapshot.

## Data-protection considerations

Any matter that involves personal data must be processed through
`data-protection-cn` (PIPL / DSL / CSL) and, if cross-border, also
through `data-protection-gdpr`. The hard-gate list catches breach
notifications and SCC filings.

## Privilege scope

PRC does not recognise attorney-client privilege in the common-law
sense; "client communications privilege" applies in narrower
settings. For cross-border investigations (FCPA, UKBA, SFC), apply
the most protective regime and document the privilege claim from
day one.

## Anti-money-laundering

Onboarding clients via `matter-intake` triggers the `kyc-onboarding`
skill if KYC has not been completed for the client. Suspicious
Activity Reports (SARs) are on the hard-gate list.
