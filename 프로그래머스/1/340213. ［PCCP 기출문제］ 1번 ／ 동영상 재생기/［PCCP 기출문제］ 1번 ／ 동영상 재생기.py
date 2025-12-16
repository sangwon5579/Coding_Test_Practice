def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    t = len(commands)
    p = to_min(pos)
    os = to_min(op_start)
    oe = to_min(op_end)
    if p >= os and p <= oe:
        answer = op_end
    else:
        answer = pos
    for i in range(t):
        if commands[i] == "next":
            answer = next_10(answer, video_len)
        else:
            answer = prev_10(answer)
        answer = jump_op(answer, op_start, op_end)
    ans = to_min(answer)
    vid = to_min(video_len)
    if ans >= vid:
        answer = video_len
    return answer

def to_min(t):
    m, s = map(int, t.split(":"))
    minute = m * 60 + s
    return minute

def to_hour(t):
    h = t // 60
    m = t - h*60
    h = str(h)
    m = str(m)
    if len(h) == 0:
        h = "00"
    if len(h) == 1:
        h = "0" + h
    if len(m) == 1:
        m = "0" + m
    ans = h + ":" + m
    return ans

def jump_op(answer, op_start, op_end):
    ans = to_min(answer)
    op_s = to_min(op_start)
    op_e = to_min(op_end)
    if ans >= op_s and ans <= op_e:
        answer = op_end
    else:
        answer = answer
    return answer

def next_10(answer, video_len):
    ans = ''
    ans_min = to_min(answer)
    ans_min += 10
    vid_min = to_min(video_len)
    if vid_min <= ans_min:
        ans = video_len
    else:
        ans = to_hour(ans_min)
    return ans

def prev_10(answer):
    ans = ''
    ans_min = to_min(answer)
    ans_min -= 10
    if ans_min <= 0:
        ans = "00:00"
    else:
        ans = to_hour(ans_min)
    return ans