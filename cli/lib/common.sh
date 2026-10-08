#!/usr/bin/env bash
# common.sh — 精益生产专家 skill 的 CLI 公共库
# 零外部依赖：纯 bash + POSIX coreutils。不要求 jq / yq / Python。

# ---------- 颜色 ----------
if [[ -t 1 ]]; then
  C_RESET=$'\033[0m'; C_BOLD=$'\033[1m'; C_DIM=$'\033[2m'
  C_RED=$'\033[31m'; C_GRN=$'\033[32m'; C_YEL=$'\033[33m'
  C_BLU=$'\033[34m'; C_CYN=$'\033[36m'
else
  C_RESET=''; C_BOLD=''; C_DIM=''
  C_RED=''; C_GRN=''; C_YEL=''; C_BLU=''; C_CYN=''
fi

# ---------- 输出 ----------
h1()    { printf '\n%s%s%s\n' "$C_BOLD$C_BLU" "$1" "$C_RESET"; }
h2()    { printf '\n%s%s%s\n' "$C_BOLD" "$1" "$C_RESET"; }
info()  { printf '%s▸%s %s\n' "$C_CYN" "$C_RESET" "$1"; }
ok()    { printf '%s✓%s %s\n' "$C_GRN" "$C_RESET" "$1"; }
warn()  { printf '%s!%s %s\n' "$C_YEL" "$C_RESET" "$1"; }
err()   { printf '%s✗%s %s\n' "$C_RED" "$C_RESET" "$1" >&2; }
dim()   { printf '%s%s%s\n' "$C_DIM" "$1" "$C_RESET"; }

# ---------- 交互 ----------
# ask <变量名> <提问> [默认值]
ask() {
  local __var="$1" __q="$2" __def="${3:-}" __ans
  if [[ -n "$__def" ]]; then
    printf '%s?%s %s [%s]: ' "$C_BOLD$C_CYN" "$C_RESET" "$__q" "$__def"
  else
    printf '%s?%s %s: ' "$C_BOLD$C_CYN" "$C_RESET" "$__q"
  fi
  IFS= read -r __ans || __ans=""
  [[ -z "$__ans" ]] && __ans="$__def"
  printf -v "$__var" '%s' "$__ans"
}

# askyn <变量名> <提问> [默认 y/n]
askyn() {
  local __var="$1" __q="$2" __def="${3:-y}" __ans
  printf '%s?%s %s [%s/n]: ' "$C_BOLD$C_CYN" "$C_RESET" "$__q" "$__def"
  IFS= read -r __ans || __ans=""
  [[ -z "$__ans" ]] && __ans="$__def"
  case "$__ans" in
    [Yy]|[Yy][Ee][Ss]) printf -v "$__var" '%s' "y" ;;
    *)                 printf -v "$__var" '%s' "n" ;;
  esac
}

# ---------- JSON 输出 ----------
# jesc <字符串> — JSON 字符串转义
jesc() {
  local s="$1"
  s="${s//\\/\\\\}"
  s="${s//\"/\\\"}"
  s="${s//$'\t'/\\t}"
  s="${s//$'\r'/\\r}"
  s="${s//$'\n'/\\n}"
  printf '%s' "$s"
}

# jnum <值> — 数字校验，非数字输出 null
jnum() {
  local v="$1"
  if [[ "$v" =~ ^-?[0-9]+(\.[0-9]+)?$ ]]; then printf '%s' "$v"; else printf 'null'; fi
}

# ---------- 报告落盘 ----------
# mdbuf_add <行>
MD_BUF=""
mdbuf_reset() { MD_BUF=""; }
mdbuf_add()   { MD_BUF+="$1"$'\n'; }
mdbuf_write() {
  local path="$1"
  printf '%s' "$MD_BUF" > "$path"
  ok "报告已写入：$path"
}

TODAY() { date +%Y-%m-%d; }

# ---------- 通用提示 ----------
require_num() {
  local v="$1" name="$2"
  if ! [[ "$v" =~ ^-?[0-9]+(\.[0-9]+)?$ ]]; then
    warn "「${name}」不是数字（输入：${v}），按0 处理并在报告中标注为缺数据。"
    printf '0'
  else
    printf '%s' "$v"
  fi
}

# 三类数字纪律：公式系数 / 某企业实测 / 未覆盖
NUMCLASS_HINT="数字纪律：区分【公式系数】/【某企业实测】/【语料未覆盖】三类，不可混用。"
