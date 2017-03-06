import SecurityNow_Class
import DownloadURL


def main():
    # initialize variables
    sn = SecurityNow_Class.SecurityNow()
    dw = DownloadURL.DownloadURL(url=None)

    try:
        no_of_ep = int(input('Download to Episode: '))
        trans = input('Download Transcripts: ').lower()
    except ValueError:
        print('Number Please for Episode')
        exit(0)

    # verify input
    if ('y' not in trans) and ('n' not in trans):
        print('Invalid input one entry.\n\tTranscript should be yes/ no.')
        exit(0)
    elif trans == 'y':
        trans = True
    elif trans == 'n':
        trans = False

    # download the episode
    for ep in range(sn.get_next_ep(), int(no_of_ep)+1):
        print('Episode ' + str(sn.get_next_ep()) + ' download...', end='', flush=True)
        dw.set_url(sn.get_url_for_next_ep().get('audio')[0])
        downloaded = dw.download_save(sn.get_url_for_next_ep().get('audio')[1])
        if downloaded:
            print(DownloadURL.BColors.OKGREEN + 'Successful.' + DownloadURL.BColors.ENDC)
            if trans:
                dw.set_url(sn.get_url_for_next_ep().get('transcript')[0])
                downloaded = dw.download_save(sn.get_url_for_next_ep().get('transcript')[1])
                if downloaded:
                    print('Transcript ' + str(sn.get_next_ep()) + ' download...', end='', flush=True)
                    print(DownloadURL.BColors.OKGREEN + 'Successful.' + DownloadURL.BColors.ENDC)
                else:
                    print(DownloadURL.BColors.WARNING + 'Failed.' + DownloadURL.BColors.ENDC)
        else:
            print(DownloadURL.BColors.WARNING + 'Failed.' + DownloadURL.BColors.ENDC)
        sn.update_current()
        sn.write_log()
    print("All Episodes Downloaded.")


if __name__ == '__main__':
    main()
