from modules import ping_services, create_team, create_sharepoint, create_powerapp, create_flow, graph_files, azure_repo
from utils.auth import get_graph_token, get_azure_pat_token

def main():
    print("=== Starting automation run ===")
    
    graph_token = get_graph_token()
    azure_pat = get_azure_pat_token()

    ping_services.ping_services()
    create_team.create_team(graph_token)
    create_sharepoint.create_sharepoint_site(graph_token)
    create_powerapp.create_powerapp(graph_token)
    create_flow.create_flow(graph_token)
    graph_files.upload_file(graph_token, "sample.txt", "AutomationFolder")
    graph_files.delete_file(graph_token, "FILE_ID")
    azure_repo.create_azure_repo(azure_pat, "my-org", "my-project", "AI-Auto-Repo")

    print("=== Automation run completed ===")

if __name__ == "__main__":
    main()
