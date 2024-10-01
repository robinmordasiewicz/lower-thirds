{{- define "video.name" -}}
{{ .Chart.Name }}
{{- end }}

{{- define "video.fullname" -}}
{{ .Release.Name }}-{{ .Chart.Name }}
{{- end }}

