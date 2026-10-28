# Flutter and iOS specialist handoffs

Use the [role](../flutter-ios-expert.agent.md) for one application or platform-boundary
change. The [Flutter skill](../../../skills/languages/flutter-patterns/SKILL.md) owns
state, navigation, lifecycle and verification guidance. Preserve the project's selected
state management and package lock; do not install a sample architecture or dependency list.

## Useful assignment

Supply the failing user journey, affected widgets/routes, Flutter/Dart and platform
versions, available simulator/device, source revision and writable scope. For a platform
channel, include both Dart and native contracts, threading expectations and error cases.

Return the change and actual analysis, widget/integration and platform-build evidence.
Name simulator/device gaps. A Dart unit test cannot establish native permission handling,
background execution, accessibility semantics or App Store acceptance.

## Focused iOS checks

- Exercise denied/revoked permissions and cancellation. Retain user data when an external
  operation fails or the app resumes from the background.
- Verify navigation and unsaved state through interruption, deep linking and restoration
  when affected. Ignore obsolete async completions after disposal or a newer request.
- Check text scaling, VoiceOver labels/actions, focus and reduced motion on the available
  target. Add semantics where built-in widgets do not already expose the intended action.
- Keep signing, entitlements, privacy declarations and native deployment targets consistent
  with the actual integration; do not claim distribution readiness from a local build.

Use current [Flutter architecture guidance](https://docs.flutter.dev/app-architecture),
[platform channels](https://docs.flutter.dev/platform-integration/platform-channels) and
[Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines/)
for an affected platform decision; load only the relevant section.
