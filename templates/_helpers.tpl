{{- define "lower-thirds.name" -}}
{{ .Chart.Name }}
{{- end }}

{{- define "lower-thirds.fullname" -}}
{{ .Release.Name }}-{{ .Chart.Name }}
{{- end }}

