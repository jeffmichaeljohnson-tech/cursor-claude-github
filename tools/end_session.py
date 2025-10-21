#!/usr/bin/env python3
"""
END OF SESSION - Complete project state preservation
Run with: python tools/end_session.py
"""

import os
import json
import subprocess
from datetime import datetime
from pathlib import Path
import sys

# Paths
RAPID_STUDIO = Path.home() / "rapid-studio"
CURSOR_CLAUDE = Path.home() / "cursor-claude-github"
CONTEXT_DIR = RAPID_STUDIO / ".claude-context"
SESSIONS_DIR = CONTEXT_DIR / "sessions"

def print_section(title):
    """Print a formatted section header"""
    print(f"\n{'='*60}")
    print(f"  {title}")
    print(f"{'='*60}\n")

def run_command(cmd, cwd=None):
    """Run a shell command and return output"""
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            cwd=cwd,
            capture_output=True,
            text=True
        )
        return result.stdout.strip()
    except Exception as e:
        return f"Error: {e}"

def get_git_status(repo_path):
    """Get comprehensive git status"""
    status = {
        "branch": run_command("git rev-parse --abbrev-ref HEAD", repo_path),
        "last_commit": run_command("git log -1 --oneline", repo_path),
        "uncommitted_changes": run_command("git status --short", repo_path),
        "total_commits_today": run_command(
            f"git log --since='midnight' --oneline | wc -l",
            repo_path
        ),
    }
    return status

def create_session_summary():
    """Create comprehensive session summary"""
    print_section("📊 GENERATING SESSION SUMMARY")
    
    timestamp = datetime.now()
    session_id = timestamp.strftime("%Y%m%d_%H%M%S")
    
    # Gather all information
    summary = {
        "session_id": session_id,
        "timestamp": timestamp.isoformat(),
        "date": timestamp.strftime("%Y-%m-%d"),
        "time": timestamp.strftime("%H:%M:%S"),
        "repositories": {
            "rapid-studio": get_git_status(RAPID_STUDIO),
            "cursor-claude-github": get_git_status(CURSOR_CLAUDE)
        }
    }
    
    # Create sessions directory
    SESSIONS_DIR.mkdir(parents=True, exist_ok=True)
    
    # Save JSON summary
    json_file = SESSIONS_DIR / f"session_{session_id}.json"
    with open(json_file, 'w') as f:
        json.dump(summary, f, indent=2)
    
    print(f"✅ Session summary saved: {json_file}")
    
    return summary, session_id

def update_master_status(summary, session_id):
    """Update the master status file"""
    print_section("📝 UPDATING MASTER STATUS")
    
    # Create context directory if it doesn't exist
    CONTEXT_DIR.mkdir(parents=True, exist_ok=True)
    
    status_file = CONTEXT_DIR / "MASTER_STATUS.md"
    
    content = f"""# Rapid Studio - Master Status

**Last Updated:** {summary['timestamp']}  
**Session ID:** {session_id}

---

## 🎯 Current State

### Rapid Studio Repository
- **Branch:** {summary['repositories']['rapid-studio']['branch']}
- **Last Commit:** {summary['repositories']['rapid-studio']['last_commit']}
- **Commits Today:** {summary['repositories']['rapid-studio']['total_commits_today']}
- **Uncommitted Changes:**
```
{summary['repositories']['rapid-studio']['uncommitted_changes'] or 'Clean working directory'}
```

### Cursor-Claude-GitHub Repository
- **Branch:** {summary['repositories']['cursor-claude-github']['branch']}
- **Last Commit:** {summary['repositories']['cursor-claude-github']['last_commit']}
- **Uncommitted Changes:**
```
{summary['repositories']['cursor-claude-github']['uncommitted_changes'] or 'Clean working directory'}
```

---

**Next Session:** Load this file first for complete context restoration!
"""
    
    with open(status_file, 'w') as f:
        f.write(content)
    
    print(f"✅ Master status updated: {status_file}")

def main():
    """Main execution"""
    print("""
    ╔══════════════════════════════════════════════════════════════╗
    ║                                                              ║
    ║              END OF SESSION - CONTEXT PRESERVATION          ║
    ║                                                              ║
    ╚══════════════════════════════════════════════════════════════╝
    """)
    
    try:
        # Create session summary
        summary, session_id = create_session_summary()
        
        # Update master status
        update_master_status(summary, session_id)
        
        print_section("✅ SESSION PRESERVATION COMPLETE")
        print(f"""
All context has been preserved!

📁 Session files created:
   • MASTER_STATUS.md (complete project state)
   • sessions/session_{session_id}.json (detailed data)

🎯 Next session: Read MASTER_STATUS.md first!

👋 Session {session_id} ended successfully.
        """)
        
    except Exception as e:
        print(f"\n❌ Error during session end: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()
