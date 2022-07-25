print("Can you hear me?")
class Solution:
    def longestPalindrome(self, s: str) -> str:
        N=len(s)
        ans=list()
        ansnum=list()
        right = N
        for i in range(N):
            left=i
            while right!=left:
                cuts = s[left:right]
                if cuts.find(cuts[::-1])!=-1 :
                    ans.append(cuts)
                    ansnum.append(right-left)
                    break
                else:
                    if right>left:right-=1
            right=N
        index=ansnum.index(max(ansnum))
        return ans[index]
a=Solution()
ans=a.longestPalindrome("bkuadixhrtfehvbjjzojfyhuqyckdeilnftnklylyssbjivhvnplrzwrgcnrciypvacbhdnglflipnlpzgivjfieunhzeaytshrintdwhbvbkhbsqbjxwhqrlneiwkmccdnfcvapmtqihzyyoiaoqgtxkpbqqdboaxmmsdjxvdrwbhdnemqmsikoksfvjjovrbgdtfgmhgryvvpunzrsluqzibsvyubyhqevpnfnszzriljpmoevpqacbvdcsgfzmnkhnshsvynxxncqyjxqazcttkvjnkuvykgdrquybvlpwzladpetocuphzkgfuutqcbnttwjmkkwbmbidcyauopcxmsarodcqabirbawtlgsytlflsiolxjghjmqrymadpzaetcchyvkaezeavjemubbquclhcjcmbwxphllhfnzfyewpyyiirgnohylfbtfddeohtifrqiiwpdtyqjyemqjlnpcwlsylxjuxtnmcrpdznbzschmnjxnldxpkbrikpfsfwhsarrfjueubvnztlwmognapvxwelyvueheqxtncpxhzwplaxqqrbmfmmqhohucxinxidxzhndvstideuwrisjgpwkgvsdxmlnfgqzzksflmjzckkyutrwptfvcawfbvqxlztstpoitdepexxiqtsdtjmssqbdinalsqkjjqkgilbfxajninuclquszwbmstcdbywfhhnierqsegafyfqzvmqockcowfqwbgfxvdxbqobditvowhtdeptljetgj")
print(ans)