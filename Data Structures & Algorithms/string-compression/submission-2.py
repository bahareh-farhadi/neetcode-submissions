class Solution:
    def compress(self, chars: List[str]) -> int:
        # use two pointers, one for read and one for write, return the last position of write at the end
        read = 0
        write = 0
        curr = None
        count = 1
        while read < len(chars):
            if curr == None:
                curr = chars[read]
            else:
                count+=1
            if read + 1 < len(chars):
                if chars[read + 1] == curr:
                    # keep reading
                    read+=1
                else:
                    # do the write
                    chars[write] = curr
                    write+=1
                    if count > 1:
                        count_s = str(count)
                        k = 0
                        while k < len(count_s):
                            chars[write] = count_s[k]
                            write+=1
                            k+=1
                    curr = None
                    count = 1
                    read+=1
            else:
                # do the write
                chars[write] = curr
                write+=1
                if count > 1:
                    count_s = str(count)
                    k = 0
                    while k < len(count_s):
                        chars[write] = count_s[k]
                        write+=1
                        k+=1
                read+=1
        return write


            

        