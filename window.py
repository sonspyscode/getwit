from tkinter import *
import hashlib
from getpass import getuser
from os import getcwd, name
from tkinter import filedialog
from getwit_pack import function
import webbrowser

window = Tk()

window.geometry("1080x796")
window.title("Getwit - Forensic Tools for Acquisition Data from Twitter")
window.iconbitmap("C:/Users/Ahmad/PycharmProjects/getwit project/win/icon/logo.ico")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 708,
    width = 1080,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

path = StringVar()
val = StringVar()
val2 = StringVar()
val3 = StringVar()
val4 = StringVar

def btn_clicked():
    print("Button Clicked")

def settext(text):
    entry0.delete(0, END)
    entry0.insert(0, text)
    return

def clearbox():
    entry0.delete(0, "end")
    entry1.delete(0, "end")
    return

def getcommand():
    result = entry0.get()
    strpar = entry1.get()
    if strpar != None:
        param = eval(strpar)

        if result == "get_tweet_lookup(tweet_ids)":
            user = function.get_tweet_lookup(param)
            print(user)

        if result == "get_tweet_by(tweet_id)":
            user = function.get_tweet_by(param)
            print(user)

        if result == "get_user_timeline(user_id)":
            user = function.get_user_timeline(param)
            print(user)

        if result == "get_user_mention_timeline(user_id)":
            user = function.get_user_mention_timeline(param)
            print(user)

        if result == "get_user_lookup_by(usernames)":
            user = function.get_user_lookup_by(param)
            print(user)

        if result == "get_my_profile()":
            user = function.get_my_profile()
            print(user)

        if result == "get_user_lookup_by_username(username)":
            user = function.get_user_lookup_by_username(param)
            print(user)

        if result == "get_users_lookup(user_ids)":
            user = function.get_users_lookup(param)
            print(user)

        if result == "get_user_lookup_by_id(user_id)":
            user = function.get_user_lookup_by_id(param)
            print(user)

        if result == "get_space_lookup(space_id)":
            user = function.get_space_lookup(param)
            print(user)

        if result == "get_search_space(str_query,state)":
            user = function.get_search_space(param[0], param[1])
            print(user)

        if result == "get_spaces(space_ids)":
            user = function.get_spaces(param)
            print(user)

        if result == "get_spaces_by_creator_ids(user_ids)":
            user = function.get_spaces_by_creator_ids(param)
            print(user)

        if result == "get_sample_stream()":
            strpar = None
            user = function.get_sample_stream()
            print(user)

        if result == "get_likes_lookup(tweet_id, max_results, pagination_token)":
            user = function.get_likes_lookup(param[0], param[1], param[2])
            print(user)

        if result == "get_liked_tweets(user_id,max_results,pagination_token)":
            user = function.get_liked_tweets(param[0], param[1], param[2])
            print(user)

        if result == "get_retweets_lookup(tweet_id, pagination_token)":
            user = function.get_retweets_lookup(param[0], param[1])
            print(user)

        if result == "get_recent_tweet_count(str_query, end_time, granularity, since_id, start_time, until_id)":
            user = function.get_recent_tweet_count(param[0],param[1],param[2],param[3],param[4],param[5])
            print(user)

        if result == "get_recent_search(str_query, end_time, max_results, next_token, since_id, start_time, until_id)":
            user = function.get_recent_search(param[0],param[1],param[2],param[3],param[4],param[5], param[6])
            print(user)

        if result == "get_quote_tweet(tweet_id, max_results, pagination_token)":
            user = function.get_quote_tweet(param[0],param[1],param[2])
            print(user)

        if result == "get_mutes_lookup(user_id, max_results, pagination_token)":
            user = function.get_mutes_lookup(param[0],param[1],param[2])
            print(user)

        if result == "user_owned_list(user_id,max_results,pagination_token)":
            user = function.user_owned_list(param[0],param[1],param[2])
            print(user)

        if result == "get_list_lookup(list_id)":
            user = function.get_list_lookup(param)
            print(user)

        if result == "get_pinned_list(user_id)":
            user = function.get_pinned_list(param)
            print(user)

        if result == "get_user_list_memberships(user_id,max_results, pagination_token)":
            user = function.get_user_list_memberships(param[0],param[1],param[2])
            print(user)

        if result == "get_list_member_lookup(list_id, max_results, pagination_token)":
            user = function.get_list_member_lookup(param[0],param[1],param[2])
            print(user)

        if result == "get_user_list_followed(user_id,max_results,pagination_token)":
            user = function.get_user_list_followed(param[0],param[1],param[2])
            print(user)

        if result == "get_list_followers_lookup(list_id, max_results, pagination_token)":
            user = function.get_list_followers_lookup(param[0],param[1],param[2])
            print(user)

        if result == "get_list_tweets(list_id, max_results, pagination_token)":
            user = function.get_list_tweets(param[0],param[1],param[2])
            print(user)

        if result == "get_following_lookup(user_id, max_results, pagination_token)":
            user = function.get_following_lookup(param[0],param[1],param[2])
            print(user)

        if result == "get_followers_lookup(user_id, max_results, pagination_token)":
            user = function.get_followers_lookup(param[0],param[1],param[2])
            print(user)

        if result == "get_block_lookup(user_id,max_results,pagination_token)":
            user = function.get_block_lookup(param[0],param[1],param[2])
            print(user)
    clearbox()

def open_file():
    global input_file
    in_path = "/home/" + getuser() if name == "posix" else getcwd
    input_file = filedialog.askopenfilename(
        initialdir=in_path, title="Select file", filetypes=[("All Files ", "*.*")]
    )
    path.set(input_file)
    calculate()

def calculate():
    md5 = hashlib.md5()
    sha256 = hashlib.sha256()
    sha1 = hashlib.sha1()
    sha512 = hashlib.sha512()

    try:
        file = open(input_file, "rb")
        data = file.read()
        sha256.update(data)
        md5.update(data)
        sha1.update(data)
        sha512.update(data)


        val.set(md5.hexdigest().upper())
        val2.set(sha256.hexdigest().upper())
        val3.set(sha256.hexdigest().upper())
        val4.set(sha256.hexdigest().upper())


    except:
        pass

def copy(item):
    window.clipboard_clear()
    window.clipboard_append(item.get())

def opendoc():
    url = "https://github.com/sonspyscode/getwit"
    webbrowser.open(url)

background_img = PhotoImage(file =f"win/background.png")
background = canvas.create_image(
    520.0, 398.0,
    image=background_img)

entry0_img = PhotoImage(file =f"win/img_textBox0.png")
entry0_bg = canvas.create_image(
    681.5, 182.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#e5e5e5",
    highlightthickness = 0)

entry0.place(
    x = 533.0, y = 165,
    width = 297.0,
    height = 32)

entry1_img = PhotoImage(file =f"win/img_textBox1.png")
entry1_bg = canvas.create_image(
    946.0, 182.0,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#e5e5e5",
    highlightthickness = 0)

entry1.place(
    x = 880.0, y = 165,
    width = 132.0,
    height = 32)

img0 = PhotoImage(file =f"win/img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = getcommand,
    relief = "flat")

b0.place(
    x = 690, y = 235,
    width = 143,
    height = 34)

entry2_img = PhotoImage(file =f"win/img_textBox2.png")
entry2_bg = canvas.create_image(
    772.5, 431.0,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#e5e5e5",
    highlightthickness = 0,
    textvariable= path)

entry2.place(
    x = 533.0, y = 414,
    width = 479.0,
    height = 32)

entry3_img = PhotoImage(file =f"win/img_textBox3.png")
entry3_bg = canvas.create_image(
    740.5, 545.0,
    image = entry3_img)

entry3 = Entry(
    bd = 0,
    bg = "#e5e5e5",
    highlightthickness = 0,
    textvariable= val)

entry3.place(
    x = 596.0, y = 528,
    width = 289.0,
    height = 32)

entry4_img = PhotoImage(file =f"win/img_textBox4.png")
entry4_bg = canvas.create_image(
    740.5, 595.0,
    image = entry4_img)

entry4 = Entry(
    bd = 0,
    bg = "#e5e5e5",
    highlightthickness = 0,
    textvariable=val2)

entry4.place(
    x = 596.0, y = 578,
    width = 289.0,
    height = 32)

img1 = PhotoImage(file =f"win/img1.png")
b1 = Button(
    image = img1,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: copy(val),
    relief = "flat")

b1.place(
    x = 908, y = 528,
    width = 121,
    height = 34)

img2 = PhotoImage(file =f"win/img2.png")
b2 = Button(
    image = img2,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: copy(val2),
    relief = "flat")

b2.place(
    x = 908, y = 578,
    width = 121,
    height = 34)

img3 = PhotoImage(file =f"win/img3.png")
b3 = Button(
    image = img3,
    borderwidth = 0,
    highlightthickness = 0,
    command = opendoc,
    relief = "flat")

b3.place(
    x = 880, y = 102,
    width = 160,
    height = 25)

img4 = PhotoImage(file =f"win/img4.png")
b4 = Button(
    image = img4,
    borderwidth = 0,
    highlightthickness = 0,
    command = open_file,
    relief = "flat")

b4.place(
    x = 659, y = 469,
    width = 205,
    height = 34)

#get function
img5 = PhotoImage(file =f"win/img5.png")
b5 = Button(
    image = img5,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: settext("get_user_lookup_by(usernames)"),
    relief = "flat")

b5.place(
    x = 55, y = 95,
    width = 359,
    height = 18)

img6 = PhotoImage(file =f"win/img6.png")
b6 = Button(
    image = img6,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: settext("get_search_space(str_query,state)"),
    relief = "flat")

b6.place(
    x = 55, y = 692,
    width = 359,
    height = 18)

img7 = PhotoImage(file =f"win/img7.png")
b7 = Button(
    image = img7,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: settext("get_my_profile()"),
    relief = "flat")

b7.place(
    x = 55, y = 113,
    width = 359,
    height = 18)

img8 = PhotoImage(file =f"win/img8.png")
b8 = Button(
    image = img8,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda: settext("get_sample_stream()"),
    relief = "flat")

b8.place(
    x = 55, y = 710,
    width = 359,
    height = 18)

img9 = PhotoImage(file =f"win/img9.png")
b9 = Button(
    image = img9,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda : settext("get_user_lookup_by_username(username)"),
    relief = "flat")

b9.place(
    x = 55, y = 131,
    width = 359,
    height = 18)

img10 = PhotoImage(file =f"win/img10.png")
b10 = Button(
    image = img10,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda : settext("get_list_lookup(list_id)"),
    relief = "flat")

b10.place(
    x = 55, y = 728,
    width = 359,
    height = 18)

img11 = PhotoImage(file =f"win/img11.png")
b11 = Button(
    image = img11,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda : settext("get_users_lookup(user_ids)"),
    relief = "flat")

b11.place(
    x = 55, y = 149,
    width = 359,
    height = 18)

img12 = PhotoImage(file =f"win/img12.png")
b12 = Button(
    image = img12,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda : settext("get_user_lookup_by_id(user_id)"),
    relief = "flat")

b12.place(
    x = 55, y = 167,
    width = 359,
    height = 18)

img13 = PhotoImage(file =f"win/img13.png")
b13 = Button(
    image = img13,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda : settext("get_followers_lookup(user_id, max_results, pagination_token)"),
    relief = "flat")

b13.place(
    x = 55, y = 184,
    width = 359,
    height = 18)

img14 = PhotoImage(file =f"win/img14.png")
b14 = Button(
    image = img14,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda : settext("get_tweet_lookup(tweet_ids)"),
    relief = "flat")

b14.place(
    x = 55, y = 250,
    width = 359,
    height = 18)

img15 = PhotoImage(file =f"win/img15.png")
b15 = Button(
    image = img15,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda : settext("get_tweet_by(tweet_id)"),
    relief = "flat")

b15.place(
    x = 55, y = 268,
    width = 359,
    height = 18)

img16 = PhotoImage(file =f"win/img16.png")
b16 = Button(
    image = img16,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda : settext("get_likes_lookup(tweet_id, max_results, pagination_token)"),
    relief = "flat")

b16.place(
    x = 55, y = 286,
    width = 359,
    height = 18)

img17 = PhotoImage(file =f"win/img17.png")
b17 = Button(
    image = img17,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda : settext("get_liked_tweets(user_id,max_results,pagination_token)"),
    relief = "flat")

b17.place(
    x = 55, y = 304,
    width = 359,
    height = 18)

img18 = PhotoImage(file =f"win/img18.png")
b18 = Button(
    image = img18,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda : settext("get_user_timeline(user_id)"),
    relief = "flat")

b18.place(
    x = 55, y = 322,
    width = 359,
    height = 18)

img19 = PhotoImage(file =f"win/img19.png")
b19 = Button(
    image = img19,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda : settext("get_user_mention_timeline(user_id)"),
    relief = "flat")

b19.place(
    x = 55, y = 340,
    width = 359,
    height = 18)

img20 = PhotoImage(file =f"win/img20.png")
b20 = Button(
    image = img20,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda : settext("get_retweets_lookup(tweet_id, pagination_token)"),
    relief = "flat")

b20.place(
    x = 55, y = 358,
    width = 359,
    height = 18)

img21 = PhotoImage(file =f"win/img21.png")
b21 = Button(
    image = img21,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda : settext("get_recent_tweet_count(str_query, end_time, granularity, since_id, start_time, until_id)"),
    relief = "flat")

b21.place(
    x = 55, y = 375,
    width = 359,
    height = 18)

img22 = PhotoImage(file =f"win/img22.png")
b22 = Button(
    image = img22,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda : settext("get_recent_search(str_query, end_time, max_results, next_token, since_id, start_time, until_id)"),
    relief = "flat")

b22.place(
    x = 55, y = 393,
    width = 359,
    height = 18)

img23 = PhotoImage(file =f"win/img23.png")
b23 = Button(
    image = img23,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda : settext("get_quote_tweet(tweet_id, max_results, pagination_token)"),
    relief = "flat")

b23.place(
    x = 55, y = 411,
    width = 359,
    height = 18)

img24 = PhotoImage(file =f"win/img24.png")
b24 = Button(
    image = img24,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda : settext("get_list_tweets(list_id, max_results, pagination_token)"),
    relief = "flat")

b24.place(
    x = 55, y = 429,
    width = 359,
    height = 18)

img25 = PhotoImage(file =f"win/img25.png")
b25 = Button(
    image = img25,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda : settext("get_space_lookup(space_id)"),
    relief = "flat")

b25.place(
    x = 55, y = 474,
    width = 359,
    height = 18)

img26 = PhotoImage(file =f"win/img26.png")
b26 = Button(
    image = img26,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda : settext("get_spaces(space_ids)"),
    relief = "flat")

b26.place(
    x = 55, y = 492,
    width = 359,
    height = 18)

img27 = PhotoImage(file =f"win/img27.png")
b27 = Button(
    image = img27,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda : settext("get_spaces_by_creator_ids(user_ids)"),
    relief = "flat")

b27.place(
    x = 55, y = 510,
    width = 359,
    height = 18)

img28 = PhotoImage(file =f"win/img28.png")
b28 = Button(
    image = img28,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda : settext("get_mutes_lookup(user_id, max_results, pagination_token)"),
    relief = "flat")

b28.place(
    x = 55, y = 528,
    width = 359,
    height = 18)

img29 = PhotoImage(file =f"win/img29.png")
b29 = Button(
    image = img29,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda : settext("user_owned_list(user_id,max_results,pagination_token)"),
    relief = "flat")

b29.place(
    x = 55, y = 546,
    width = 359,
    height = 18)

img30 = PhotoImage(file =f"win/img30.png")
b30 = Button(
    image = img30,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda : settext("get_pinned_list(user_id)"),
    relief = "flat")

b30.place(
    x = 55, y = 564,
    width = 359,
    height = 18)

img31 = PhotoImage(file =f"win/img31.png")
b31 = Button(
    image = img31,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda : settext("get_user_list_memberships(user_id,max_results, pagination_token)"),
    relief = "flat")

b31.place(
    x = 55, y = 582,
    width = 359,
    height = 18)

img32 = PhotoImage(file =f"win/img32.png")
b32 = Button(
    image = img32,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda : settext("get_list_member_lookup(list_id, max_results, pagination_token)"),
    relief = "flat")

b32.place(
    x = 55, y = 600,
    width = 359,
    height = 18)

img33 = PhotoImage(file =f"win/img33.png")
b33 = Button(
    image = img33,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda : settext("get_user_list_followed(user_id,max_results,pagination_token)"),
    relief = "flat")

b33.place(
    x = 55, y = 618,
    width = 359,
    height = 18)

img34 = PhotoImage(file =f"win/img34.png")
b34 = Button(
    image = img34,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda : settext("get_list_followers_lookup(list_id, max_results, pagination_token)"),
    relief = "flat")

b34.place(
    x = 55, y = 636,
    width = 359,
    height = 18)

img35 = PhotoImage(file =f"win/img35.png")
b35 = Button(
    image = img35,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda : settext("get_following_lookup(user_id, max_results, pagination_token)"),
    relief = "flat")

b35.place(
    x = 55, y = 202,
    width = 359,
    height = 18)

img36 = PhotoImage(file =f"win/img36.png")
b36 = Button(
    image = img36,
    borderwidth = 0,
    highlightthickness = 0,
    command = lambda : settext("get_block_lookup(user_id,max_results,pagination_token)"),
    relief = "flat")

b36.place(
    x = 55, y = 654,
    width = 359,
    height = 18)

window.resizable(False, False)
window.mainloop()
